# -*- coding: utf-8 -*-
import numpy as np
import cv2
from Tkinter import *
import time
import matplotlib.pylab as plt
import socket
import subprocess
import smtplib
import sqlite3
import os.path
import os
import time
from datetime import date, datetime
import ftplib

#Grabación de imagenes y reconocimiento facial
def grabacion():
	extension = 'tiff'
	con = 0 		 
	#cargamos la plantilla e inicializamos la webcam:
	face_cascade = cv2.CascadeClassifier('/home/shinigami/data/haarcascades/haarcascade_frontalface_alt.xml')
	eye_cascade = cv2.CascadeClassifier('/home/shinigami/data/haarcascades/haarcascade_eye.xml')
	cap = cv2.VideoCapture(0)

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
		for r in range(5):
			nombre = ''
			nombre = str(con)+"."+extension
			cv2.imwrite(nombre,frame)
			con= 0
			con2 = 0	
			extension = 'tiff'
			dia = datetime.now()

			conexion = sqlite3.connect('/home/shinigami/Documentos/InterfazDron/base.db', timeout=100)
			cursor = conexion.cursor()
			cursor.execute('CREATE TABLE IF NOT EXISTS video2(id INTERGER PRIMARY KEY ,imagen BLOB NOT NULL,fecha DATE NOT NULL)')
			for x in range(1, 1000):
				#time.sleep(2)
				con+= 1
				nombre=''
				nombre = str(con)+"."+extension
				if os.path.exists(nombre):
					imagenes = open(nombre, 'r').read()
					print 'El archivo existe ✌.|•͡˘‿•͡˘|.✌'
					buff = sqlite3.Binary(imagenes)	 
					cursor.execute('INSERT INTO video2(imagen,fecha) VALUES(?,?)', (buff,dia,))
		
				else:
					break
	
			conexion.commit()
	
			for x in range(1, 1000):
				con2+= 1
				nombre2 = ''
				nombre2 = str(con2)+"."+extension
				print nombre2
				if os.path.exists(nombre2):
					os.remove(nombre2)
					print'Eliminación de archivos concretada (づ｡◕‿‿◕｡)づ'
				else:
					break
			conexion.close()
	#con la tecla 'q' salimos del programa
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cap.release()
	cv2.destroyAllWindows()
	
#Función de calculos de diferencias de pixeles
def diffImg(i0,i1,i2):
    d1 = cv2.absdiff(i2, i1)
    d2 = cv2.absdiff(i1, i0)
    return cv2.bitwise_and(d1, d2)
"""captura = cv2.VideoCapture(0)
def getImg():
    return cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)"""

#Función de grabación de movimiento    
def movimiento():
	captura = cv2.VideoCapture(0)
	cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t1 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t2 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
	t3 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)

	movimientonivel = 0
	extension2 = 'tiff'
	con2 = 500000
	x= 0
	while True:
		
		diff = diffImg(t1, t2, t3)
		ret, diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
		nz = cv2.countNonZero(diff) * 1.
		height, width = diff.shape

		if movimientonivel < 40:
			movimientonivel+=nz/(height * width) * 2000
		if movimientonivel > 0:
			movimientonivel-=1;

		if movimientonivel > 10:
			#time.sleep(1)
			con2+= 1
			#x+=1
			print "Movimiento:", movimientonivel
			nombre2=''
			nombre2= str(con2)+"."+extension2
			cv2.imwrite(nombre2,diff)

		cv2.imshow('frame', diff)
		#Cuenta pixeles
		t1 = t2
		t2 = t3
		#t3 = getImg()
		t3 = cv2.cvtColor(captura.read()[1], cv2.COLOR_BGR2GRAY)
   
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break;

	captura.release()
	cv2.destroyAllWindows()

#Funcion que almacena y elimina todas las imagenes	
def almacena_elimina():
	con= 0
	con2 = 0
	cont3 = 500000
	cont4 = 500000
	extension = 'tiff'
	dia = datetime.now()

	conexion = sqlite3.connect('/home/shinigami/Documentos/InterfazDron/base.db', timeout=100)
	cursor = conexion.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS video2(id INTERGER PRIMARY KEY ,imagen BLOB NOT NULL,fecha DATE NOT NULL)')
	for x in range(1, 1000):
		#time.sleep(2)
		con+= 1
		nombre=''
		nombre = str(con)+"."+extension
		if os.path.exists(nombre):
			imagenes = open(nombre, 'r').read()
			print 'El archivo existe ✌.|•͡˘‿•͡˘|.✌'
			buff = sqlite3.Binary(imagenes)	 
			cursor.execute('INSERT INTO video2(imagen,fecha) VALUES(?,?)', (buff,dia,))
		
		else:
			break
	
	conexion.commit()
	

	for x in range(1, 1000):
		con2+= 1
		nombre2 = ''
		nombre2 = str(con2)+"."+extension
		print nombre2
		if os.path.exists(nombre2):
			os.remove(nombre2)
			print'Eliminación de archivos concretada (づ｡◕‿‿◕｡)づ'
		else:
			break
	for x in range(500000, 1000000):
		#time.sleep(2)
		cont3+= 1
		nombre3=''
		nombre3 = str(cont3)+"."+extension
		if os.path.exists(nombre3):
			imagenes2 = open(nombre3, 'r').read()
			print 'El archivo existe ⊂(◉‿◉)つ'
			buff = sqlite3.Binary(imagenes2)	 
			cursor.execute('INSERT INTO video2(imagen,fecha) VALUES(?,?)', (buff,dia,))
		else:
			break
		
	conexion.commit()

	for x in range(500000, 1000000):
		cont4+= 1
		nombre4 = ''
		nombre4 = str(cont4)+"."+extension
		print nombre4
		if os.path.exists(nombre4):
			os.remove(nombre4)
			print'Eliminación de archivos concretada ஜ۩۞۩ஜ ▂ ▃ ▅ ▆ █ █ ▆ ▅ ▃ ▂'
		else:
			break
	conexion.close()	

def actualiza():
	while True():
		time.sleep(60)
		# Datos FTP
		ftp_servidor = 'ftp.pc-rescue-and-careful.com'
		ftp_usuario  = 'pcrescuecommx'
		ftp_clave    = '91Pc-r'
		ftp_raiz     = '/CUSA' # Carpeta del servidor donde queremos subir el fichero
		# Datos del fichero a subir
		fichero_origen = '/home/shinigami/Documentos/InterfazDron/base.db' # Ruta al fichero que vamos a subir
		fichero_destino = 'base' # Nombre que tendrá el fichero en el servidor 
		# Conectamos con el servidor
		try:
			s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
			try:
				f = open(fichero_origen, 'rb')
				s.cwd(ftp_raiz)
				s.storbinary('STOR ' + fichero_destino, f)
				f.close()
				s.quit()
			except:
				print "No se ha podido encontrar el fichero " + fichero_origen
		except:
			print "No se ha podido conectar al servidor " + ftp_servidor
			print "La Base de datos a sido actualizada"
	
def detectaColor():
	#Iniciamos la camara
	captura = cv2.VideoCapture(0)
	while(1):     
		#Capturamos una imagen y la convertimos de RGB -> HSV
		i, imagen = captura.read()
		hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
		#Establecemos el rango de colores que vamos a detectar
		#En este caso de verde oscuro a verde-azulado claro
		verde_bajos = np.array([49,50,50], dtype=np.uint8)
		verde_altos = np.array([80, 255, 255], dtype=np.uint8)
		amarillo_altos = np.array([35,255,255], dtype=np.uint8)
		amarillo_bajos = np.array([20,20,20], dtype =np.uint8)
		negro =  np.array([103,86,65], dtype=np.uint8)
		negro_fuerte = np.array([145,133,128], dtype=np.uint8)
		blanco_bajo = np.array([0, 0, 166], dtype= np.uint8)
		blanco_fuerte = np.array([180, 53, 255], dtype=np.uint8)
		rojo_bajo = np.array([0, 90, 60], dtype=np.uint8)
		rojo_fuerte = np.array([10, 255, 255], dtype=np.uint8)
		#Crear una mascara con solo los pixeles dentro del rango de verdes
		mask = cv2.inRange(hsv, rojo_bajo, rojo_fuerte)
 
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
	
inicio = Tk()

inicio.title('CUSA RADXA')
inicio.geometry('780x380')

boton1=Button(inicio, text='Grabado y Reconocimiento', command=grabacion)
boton1.grid(row=1,column=1)
boton1=Button(inicio, text='Detección de Movimiento', command=movimiento)
boton1.grid(row=1,column=2)
boton1=Button(inicio, text='Almacenamiento y borrado de archivos', command=almacena_elimina)
boton1.grid(row=1,column=3)
boton1=Button(inicio, text='Deteccion de alto', command=detectaColor)
boton1.grid(row=1,column=4)

inicio.mainloop()
