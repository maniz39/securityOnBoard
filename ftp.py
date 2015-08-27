#!/usr/bin/env python
# -*- coding: cp1252 -*-
import ftplib
import os
import time

 

while True:
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
