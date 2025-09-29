import cv2 
import numpy as np

#Captura de vídeo da webcam
cap = cv2.VideoCapture(0)


while True:
    _, frame = cap.read()
    
    #Converte RGB para HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Máscara Vermelha
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    #Máscara Azul
    low_blue = np.array([95, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    
    #Máscara Verde
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    
    #Vermelho OU Azul (bitwise_or)
    red_or_blue_mask = cv2.bitwise_or(red_mask, blue_mask)
    red_or_blue_result = cv2.bitwise_and(frame, frame, mask=red_or_blue_mask)
    
    #Verde E Azul (bitwise_and) - raramente vai aparecer algo
    green_and_blue_mask = cv2.bitwise_and(green_mask, blue_mask)
    green_and_blue_result = cv2.bitwise_and(frame, frame, mask=green_and_blue_mask)
    
    #Tudo EXCETO vermelho (bitwise_not)
    not_red_mask = cv2.bitwise_not(red_mask)
    not_red_result = cv2.bitwise_and(frame, frame, mask=not_red_mask)
    
    #(Azul OU Verde) E NÃO Vermelho
    blue_or_green = cv2.bitwise_or(blue_mask, green_mask)
    complex_mask = cv2.bitwise_and(blue_or_green, not_red_mask)
    complex_result = cv2.bitwise_and(frame, frame, mask=complex_mask)
    
    cv2.imshow("1. Original", frame)
    cv2.imshow("2. Vermelho OU Azul", red_or_blue_result)
    cv2.imshow("3. Verde E Azul", green_and_blue_result)
    cv2.imshow("4. Tudo EXCETO Vermelho", not_red_result)
    cv2.imshow("5. (Azul OU Verde) E NAO Vermelho", complex_result)
    
    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
print("Programa encerrado!")
