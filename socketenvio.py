# -*- coding: utf-8 -*-
import sqlite3
import os.path
import os
import time
from datetime import date, datetime
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
		print 'El archivo existe'
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
		print'Eliminación de archivos concretada'
	else:
		break
		
for x in range(500000, 1000000):
	#time.sleep(2)
	cont3+= 1
	nombre3=''
	nombre3 = str(cont3)+"."+extension
	if os.path.exists(nombre3):
		imagenes2 = open(nombre3, 'r').read()
		print 'El archivo existe'
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
		print'Eliminación de archivos concretada'
	else:
		break
conexion.close()	







