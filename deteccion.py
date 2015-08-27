import numpy as np
import cv2
from Tkinter import *
import time

extension = 'png'
punto = '.'
salto = "\n"
			 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('/home/shinigami/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/shinigami/data/haarcascades/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

con = 0 
while(True):
	con += 1
    #leemos un frame y lo guardamos
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = np.array(gray, dtype='uint8')
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w,y+h) , (255,0,0) , 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #Mostramos la imagen
	cv2.imshow('img',frame)
  
    #Se escribe la imagen y se bajo el rango
	for r in range(8):
			nombre = ''
			nombre = str(con)+"_"+str(r)+"."+extension
			cv2.imwrite(nombre,frame)
	
   #cv2.imwrite(nombre,img)
#con la tecla 'q' salimos del programa
	if cv2.waitKey(1) & 0xFF == ord('q'):
			break
cap.release()
cv2-destroyAllWindows()

