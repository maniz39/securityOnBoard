# -*- coding: utf-8 -*-
import sqlite3

nombre=''
conta = 0
extension = 'tiff'
conexion = sqlite3.connect('base.db', timeout=100)
c = conexion.cursor()
par = (1,)
a = c.execute("SELECT imagen FROM video2 WHERE imagen>?", par)
for x in a:
	a = c.fetchone() # Lee el primer registro
	img = a
	img = img[0]
	print len(img)
	conta += 1
	nombre = str(conta)+"."+extension
	f= open(nombre, 'w')
	f.write(img)
	f.close()
	print 'Fue todo un puto exito ┌∩┐(◕_◕)┌∩┐'
	print conta
	#delete = c.execute("DELETE FROM video2 WHERE rowid>=?", (conta,))


