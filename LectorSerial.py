#!/usr/bin/python
import serial
import sqlite3
import time
from Tkinter import *
from datetime import date, datetime
#Detectara si es desconectado el sensor o el arduino

PuertoSerie = serial.Serial('/dev/ttyACM1', 9600)
dia = datetime.now()
desconexion = time.strftime("%H:%M:%S") 
while True:
  sArduino = PuertoSerie.readline()
  # Mostramos el valor leido y eliminamos el salto de linea del final
  print "Valor Arduino: " + sArduino.rstrip('\n')
  conexion = sqlite3.connect('home/manuel/Documentos/InterfazDron/lectura.db', timeout=100)
  cursor = conexion.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS lectura(id INTERGER PRIMARY KEY ,lector VARCHAR(5) NOT NULL,fecha DATE NOT NULL,unidad VARCHAR (15) NOT NULL, desconexion TIME NOT NULL)')
  cursor.execute('INSERT INTO lectura(lector,fecha,unidad) VALUES(?,?)', (sArduino,dia,))
  if sArduino == null :
	  cursor.execute('INSERT INTO lectura(fecha,desconexion) VALUES(?,?)', (dia,desconexion,))
	  conexion.commit()

conexion.commit()
