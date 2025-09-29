#Importação das bibliotecas
import cv2 
import numpy as np

#Instanciação da webcam
cap = cv2.VideoCapture(0)

#loop infinito para webcam ficar aberta
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Cor vermelha
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)

    #Cor azul
    low_blue = np.array([95,80,2])
    high_blue = np.array([126,255,255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

    #Cor verde
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    gren_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask = gren_mask)

    #Todas as cores exceto branco
    low = np.array([0,42,0])
    high = np.array([179,255,255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Resultado sem branco", result)
    
    key = cv2.waitKey(1)
    if key == 27:
         break
    
