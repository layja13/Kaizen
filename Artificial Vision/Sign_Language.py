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
                              max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

window = "Hands detection"
cv2.namedWindow(window, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window, 720, 420)

while True:

    ret, frame = cap.read()

    RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands_object.process(RGB_frame)

    if results.multi_hand_landmarks:
        for points in results.multi_hand_landmarks:
            #mp_dibujo.draw_landmarks(frame, points, mp_manos.HAND_CONNECTIONS)
            dedo_pulgar = points.landmark[4]
            dedo_indice = points.landmark[8]
            dedo_medio = points.landmark[12]
            dedo_anular = points.landmark[16]
            dedo_menique = points.landmark[20]
            central_point = points.landmark[5]

            alto, ancho, canales = frame.shape

            all_landmarks_pos = []

            for i in range(len(points.landmark)):
                all_landmarks_pos.append((int(points.landmark[i].x*ancho), int(points.landmark[i].y*alto)))
                #cv2.circle(frame, (all_landmarks_pos[i][0], all_landmarks_pos[i][1]), 15, (255,0,0), thickness=-1)

            if all_landmarks_pos[12][0] > all_landmarks_pos[11][0] and all_landmarks_pos[11][1] < all_landmarks_pos[9][1] and all_landmarks_pos[12][1] > all_landmarks_pos[11][1]:
                gesto = "O"
                print(gesto)
    
            elif all_landmarks_pos[4][0] < all_landmarks_pos[5][0] and (all_landmarks_pos[8][1] and all_landmarks_pos[12][1] and all_landmarks_pos[16][1]) > all_landmarks_pos[9][1] and all_landmarks_pos[18][1] > all_landmarks_pos[20][1] :
                gesto = "I"
                print(gesto)

            elif all_landmarks_pos[4][0] < all_landmarks_pos[5][0] and (all_landmarks_pos[8][1] and all_landmarks_pos[12][1]) < all_landmarks_pos[10][1] and (all_landmarks_pos[16][1] and all_landmarks_pos[20][1]) > all_landmarks_pos[4][1]:
                gesto = "U"
                print(gesto)

            elif all_landmarks_pos[4][0] < all_landmarks_pos[6][0] and (all_landmarks_pos[8][1] and all_landmarks_pos[12][1] and all_landmarks_pos[16][1] and all_landmarks_pos[20][1]) > all_landmarks_pos[9][1] and (all_landmarks_pos[7][1] and all_landmarks_pos[11][1] and all_landmarks_pos[15][1] and all_landmarks_pos[19][1]) < all_landmarks_pos[4][1]:
                gesto = "E"
                print(gesto)

            elif  all_landmarks_pos[4][0] > all_landmarks_pos[6][0] and (all_landmarks_pos[8][1] and all_landmarks_pos[12][1] and all_landmarks_pos[16][1] and all_landmarks_pos[20][1]) > all_landmarks_pos[9][1]:
                gesto = "A"
                print(gesto)

            else:
                gesto = "Gesto no detectado"
                print(gesto)
                
            
        cv2.putText(frame,f"Gesto detectado: {gesto}", (30,50), cv2.FONT_ITALIC, 1, (255,100,0), thickness=3)

        try:
            arduino.write(f"{gesto}A\n".encode())
        except:
            pass
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
