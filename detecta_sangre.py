import numpy as np
import cv2

captura = cv2.VideoCapture(0)
 
while (1):
	_, imagen = captura.read()
	hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
	
	lower_red = np.array([0, 90, 60], dtype=np.uint8)
	upper_red = np.array([10, 255, 255], dtype=np.uint8)
    #Crear una mascara con solo los pixeles dentro del rango de verdes
	mask = cv2.inRange(hsv, lower_red, upper_red)
 
    #Encontrar el area de los objetos que detecta la camara
	moments = cv2.moments(mask)
	area = moments['m00']
 
    #Descomentar para ver el area por pantalla
    #print area
	if(area > 2000000):
       #Buscamos el centro x, y del objeto
		x = int(moments['m10']/moments['m00'])
		y = int(moments['m01']/moments['m00'])
         
        #Mostramos sus coordenadas por pantalla
		print "x = ", x
		print "y = ", y
 
        #Dibujamos una marca en el centro del objeto
		cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
     
     
    #Mostramos la imagen original con la marca del centro y
    #la mascara
	cv2.imshow('mask', mask)
	cv2.imshow('Camara', imagen)
	
	tecla = cv2.waitKey(5) & 0xFF
	if tecla == 27:
		break
 
	cv2.destroyAllWindows()
