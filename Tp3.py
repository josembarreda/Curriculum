import tkinter as tk
from tkinter import simpledialog


fi=open('file.txt','r')
fh=open('Respuestas','w')
vent=tk.Tk()
preg=fi.readline()
window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Nombre y Apellidos: ', window.capitalize())
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Fecha de nacimiento: ', window)
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('DNI/NIF: ', window)
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Direccion: ', window)
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askinteger('Input',preg,
	                        parent=vent,
	                        minvalue=10000, maxvalue=99999)

if window is not None:
	print('Codigo Postal: ', window)
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

print('---------------Datos Personales----------------' + '\n')


window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Titulos Academicos: ', window)
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Instituto/s de formación: IES.', window.capitalize())
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print('Experiencia Laboral:', window.capitalize())
	fh.write(str(window + '\n'))
else:
	pass
preg=fi.readline()
print('----------------Datos Laborales-----------------' + '\n')

window= simpledialog.askstring('Input',preg,
	                        parent=vent)

if window is not None:
	print(window.capitalize())
	fh.write(str(window + '\n'))
else:
	pass

print('----------------Aspiraciones-----------------' '\n')
print('Creando Curriculum Vitae...')
fi.close()
fh.close()