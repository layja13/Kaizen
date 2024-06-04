import mediapipe as mp
import cv2
import serial

mp_dibujo = mp.solutions.drawing_utils
mp_manos = mp.solutions.hands

try:
    arduino = serial.Serial("COM8", 9600, timeout=1)
except:
    print("No connection to Arduino")


hands_object = mp_manos.Hands(static_image_mode=False,
                              max_num_hands=2, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

window = "Hands detection"
cv2.namedWindow(window, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window, 720, 420)


check_pulgar = 0
check_indice = 0
check_medio = 0
check_anular = 0
check_menique = 0


while True:

    ret, frame = cap.read()

    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands_object.process(RGB_frame)

    if results.multi_hand_landmarks:
        for points in results.multi_hand_landmarks:
            # mp_dibujo.draw_landmarks(frame, points, mp.manos.HAND_CONNECTIONS)
            dedo_pulgar = points.landmark[4]
            dedo_indice = points.landmark[8]
            dedo_medio = points.landmark[12]
            dedo_anular = points.landmark[16]
            dedo_menique = points.landmark[20]
            central_point = points.landmark[5]

            alto, ancho, canales = frame.shape

            pulgarX, pulgarY = int(dedo_pulgar.x*ancho), int(dedo_pulgar.y*alto)
            indiceX, indiceY = int(dedo_indice.x*ancho), int(dedo_indice.y*alto)
            medioX, medioY = int(dedo_medio.x*ancho), int(dedo_medio.y*alto)
            anularX, anularY = int(dedo_anular.x*ancho), int(dedo_anular.y*alto)
            meniqueX, meniqueY = int(dedo_menique.x*ancho), int(dedo_menique.y*alto)
            centralX, centralY = int((central_point.x*ancho)*0.95), int((central_point.y*alto)*0.9)

            cv2.circle(frame, (indiceX,indiceY), 15, (255,0,0), thickness=-1)
            cv2.circle(frame, (pulgarX,pulgarY), 15, (255,0,0), thickness=-1)
            cv2.circle(frame, (medioX,medioY), 15, (255,0,0), thickness=-1)
            cv2.circle(frame, (anularX,anularY), 15, (255,0,0), thickness=-1)
            cv2.circle(frame, (meniqueX,meniqueY), 15, (255,0,0), thickness=-1)
            cv2.circle(frame, (centralX,centralY), 15, (0,0,255), thickness=-1)

            if pulgarX < centralX:
                check_pulgar = 1
            else:
                check_pulgar = 0

            if indiceY < centralY:
                check_indice = 1
            else:
                check_indice = 0

            if medioY < centralY:
                check_medio = 1
            else:
                check_medio = 0

            if anularY < centralY:
                check_anular = 1
            else:
                check_anular = 0

            if meniqueY < centralY:
                check_menique = 1
            else:
                check_menique = 0
            
            sum =  check_pulgar + check_indice + check_medio + check_anular + check_menique 
            print(sum)
            
        cv2.putText(frame,f"Detected fingers: {sum}", (30,50), cv2.FONT_ITALIC, 1, (255,100,0), thickness=3)

        try:
            arduino.write(f"{check_pulgar}A{check_indice}B{check_medio}C{check_anular}D{check_menique}\n".encode())
        except:
            print("No connection to arduino")
    else:
        cv2.putText(frame, f"No detected", (30,50), cv2.FONT_ITALIC, 1, (0,0,255), thickness=3)
        sum=0

    cv2.imshow(window, frame)
    out = cv2.waitKey(1)
    if out == 27:
        break

cap.release()
cv2.destroyAllWindows()
