import cv2
import mediapipe as mp
import numpy as np
import math
import serial

# Inicializar el módulo de detección de pose de Mediapipe
mp_pose = mp.solutions.pose
mp_dibujo = mp.solutions.drawing_utils

# Asignar el modelo a la variable pose
objeto_pose = mp_pose.Pose(static_image_mode=False,
                           min_detection_confidence=0.5, 
                           min_tracking_confidence=0.5)

# Inicializar la cámara
cap = cv2.VideoCapture(0)  # Cambiado a 0 para usar la cámara predeterminada

try:
    arduino = serial.Serial("COM8", 9600, timeout=1)
except:
    print("No se pudo conectar")

ventana1 = "captura"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)

while True:
    ret, frame = cap.read()  # Capturar un fotograma

    # Convertir a formato RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Obtener resultados de la detección de pose
    resultados = objeto_pose.process(rgb_frame)

    # Verificar si se detectó una pose
    if resultados.pose_landmarks:
        for puntos in [resultados.pose_landmarks]:
            # Dibujar landmarks y conexiones
            #mp_dibujo.draw_landmarks(frame, puntos, mp_pose.POSE_CONNECTIONS)

            alto, ancho, canales = frame.shape

            #triang 1
            hombro = (int(puntos.landmark[11].x*ancho), int(puntos.landmark[11].y*alto))
            muneca = (int(puntos.landmark[15].x*ancho), int(puntos.landmark[15].y*alto))
            codo = (int(puntos.landmark[13].x*ancho), int(puntos.landmark[13].y*alto))

            dist_hombro_codo = (hombro[0] - codo[0], hombro[1] - codo[1])
            dist_codo_muneca = (codo[0] - muneca[0], codo[1] - muneca[1])
            dist_muneca_hombro = (hombro[0] - muneca[0], hombro[1] - muneca[1])

            dist_hombro_codo = np.sqrt(dist_hombro_codo[0]**2 + dist_hombro_codo[1]**2)
            dist_codo_muneca = np.sqrt(dist_codo_muneca[0]**2 + dist_codo_muneca[1]**2)
            dist_muneca_hombro = math.sqrt(dist_muneca_hombro[0]**2 + dist_muneca_hombro[1]**2)

            angulo_codo = int(math.degrees(math.acos((dist_hombro_codo**2+dist_codo_muneca**2-dist_muneca_hombro**2)/(2*dist_hombro_codo*dist_codo_muneca))))

            cv2.circle(frame,(hombro[0], hombro[1]), 15, (0,255,0), thickness=-1)
            cv2.circle(frame,(codo[0], codo[1]), 15, (0,255,0), thickness = -1)
            cv2.circle(frame,(muneca[0], muneca[1]), 15, (0,255,0), thickness = -1)
                     
            cv2.line(frame, hombro, codo, (0,255,0), thickness = 5)
            cv2.line(frame, codo, muneca, (0,255,0), thickness = 5)
            cv2.line(frame,muneca, hombro, (0,255,0), thickness = 5)

            #print("hombro_codo:",dist_hombro_codo,"  |codo_muneca:", dist_codo_muneca,"  |muneca_hombro:", dist_muneca_hombro)

            print("angulo_codo:", angulo_codo)

            #print(angulo1)

            #triang 2
            cadera = (int(puntos.landmark[23].x*ancho), int(puntos.landmark[23].y*alto))

            dist_hombro_cadera = (hombro[0] - cadera[0], hombro[1] - cadera[1])
            dist_codo_cadera = (codo[0] - cadera[0], codo[1] - cadera[1])

            dist_hombro_cadera = np.sqrt(dist_hombro_cadera[0]**2 + dist_hombro_cadera[1]**2)
            dist_codo_cadera = np.sqrt(dist_codo_cadera[0]**2 + dist_codo_cadera[1]**2)

            angulo_cadera = int(math.degrees(math.acos((dist_hombro_cadera**2+dist_hombro_codo**2-dist_codo_cadera**2)/(2*dist_hombro_cadera*dist_hombro_codo))))

            cv2.circle(frame,(cadera[0], cadera[1]), 15, (0,255,0), thickness = -1)
                     
            cv2.line(frame, codo, cadera, (0,255,0), thickness = 5)
            cv2.line(frame,cadera, hombro, (0,255,0), thickness = 5)

            cv2.putText(frame, str(angulo_codo),(codo[0],codo[1]),cv2.FONT_ITALIC, 2, (255,0,0), thickness=7)
            cv2.putText(frame, str(angulo_cadera),(hombro[0],hombro[1]),cv2.FONT_ITALIC, 2, (255,0,0), thickness=7)

            try:
                arduino.write(f"{angulo_codo}A{angulo_cadera}B{alto}\n".encode())
            except:
                print("No se envian datos !!")

    # Mostrar el fotograma
    cv2.imshow(ventana1, frame)

    # Salir del bucle si se presiona la tecla 'q'
    salir = cv2.waitKey(1)
    if salir == 27:
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
