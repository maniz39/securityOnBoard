#!/usr/bin/python
import serial
import sqlite3
import time
from Tkinter import *
from datetime import date, datetime

PuertoSerie = serial.Serial('/dev/ttyACM1', 9600)
dia = datetime.now()
while True:
  conexion = sqlite3.connect('home/manuel/Documentos/InterfazDron/lectura.db', timeout = 100)
  cursor = conexion.cursor()
  cursor.execute('CREATE TABLE IF NOT EXISTS video2(id INTERGER PRIMARY KEY ,lector FLOAT NOT NULL,fecha DATE NOT NULL,unidad VARCHAR NOT NULL)')
  
  
  sArduino = PuertoSerie.readline()
  # Mostramos el valor leido y eliminamos el salto de linea del final
  print "Valor Arduino: " + sArduino.rstrip('\n')
