import sys
import time
import tkinter 

from tkinter import *
ventana = tkinter.Tk()
lienzo = Canvas(ventana, width = 400, height = 400)
lienzo.pack()
lienzo.create_oval(10,10,50,50, fill = "blue")

def movimiento():
    for x in range(0,60):
      lienzo.move(1,5,0)
      ventana.update()
      time.sleep(0.05)

boton = tkinter.Button(text="ale", command=movimiento)
boton.pack()

"""def movimiento( ):
  for x in range(0,60):
    lienzo.move(1,5,0)
    ventana.update()
    time.sleep(0.05)"""


ventana.mainloop()





"""from tkinter import*
ventana = Tk()
ventana.geometry("700x600+0+0")
imagenF=PhotoImage(file="flecha.gif")
lblImagen=Label(ventana, image=imagenF).place(x=100, y=100)

for x in range(0,60):
    .move(1,5,0)
    ventana.update()
    time.sleep(0.05)

ventana.mainloop()"""


