import cv2
import numpy as np
import serial  

cap = cv2.VideoCapture(0)

window_1 = "Capture"
cv2.namedWindow(window_1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_1, 720, 420)

window_2 = "Mask"
cv2.namedWindow(window_2, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_2, 720, 420)

text1 = "Detected colour"
text2 = "No detected"

try:
    arduino = serial.Serial("COM8", 9600, timeout=1)
except:
    print("No connection to Arduino")



while True:

    _, frame = cap.read()

    hsv_video = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    colorMin = np.array([0, 168, 80])
    colorMax = np.array([25, 255, 255])


    mask = cv2.inRange(hsv_video, colorMin, colorMax)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        max_contours = max(contours, key=cv2.contourArea)
        (x,y) , radius = cv2.minEnclosingCircle(max_contours)
        x = int(x)
        y = int(y)
        radius = int(radius)
        print(radius)

        if radius > 25:
            cv2.circle(frame, (x,y), radius, (255,0,0), thickness=5)   
            cv2.putText(frame, text1, (10, 50), cv2.FONT_ITALIC, 1, (255,0,0), thickness=3)
            #cv2.drawContours(frame, max_contours, -1, (0,255,0), 3)
            try:
                arduino.write(f"{x}A{y}\n".encode())
            except:
                pass

        else:
            cv2.putText(frame, text2, (10, 50), cv2.FONT_ITALIC, 1, (0,0,255), thickness=3)
 


    cv2.imshow(window_1, frame)
    cv2.imshow(window_2, mask)

    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()
