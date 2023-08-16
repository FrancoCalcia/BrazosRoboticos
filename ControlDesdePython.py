# Importar las bibliotecas necesarias
from tkinter import *
from time import sleep
from pyfirmata import Arduino, SERVO

# Configuración de la placa Arduino
board = Arduino('COM5')  # Cambiar 'COM5' al puerto correcto
sleep(5)  # Esperar para que la placa Arduino se inicialice

# Definir los pines a los que se conectan los servos
pinS1 = 2  # Base
pinS2 = 3  # Codo
pinS3 = 4  # Muñeca
pinS4 = 5  # Gripper

# Configurar los pines como salidas para los servos
board.digital[pinS1].mode = SERVO
board.digital[pinS2].mode = SERVO
board.digital[pinS3].mode = SERVO
board.digital[pinS4].mode = SERVO

# Funciones para mover los servos
def servo1(posiciones1):
    board.digital[pinS1].write(posiciones1)  # Mover el servo de la base

def servo2(posiciones2):
    board.digital[pinS2].write(posiciones2)  # Mover el servo del codo

def servo3(posiciones3):
    board.digital[pinS3].write(posiciones3)  # Mover el servo de la muñeca

def servo4(posiciones4):
    board.digital[pinS4].write(posiciones4)  # Mover el servo del gripper

# Crear la ventana principal de la interfaz gráfica
root = Tk()
root.title("Control de Brazo Robótico")
root.minsize(800, 450)


# Crear etiquetas y configurarlas
var = StringVar()
etiqueta = Label(root, textvariable=var, relief=FLAT, pady=5, font=('Georgia'))
var.set("Interfaz gráfica de usuario\n para el manejo\n del brazo robótico")
etiqueta.grid(column=1, row=1)

var2 = StringVar()
etiquetaAp = Label(root, textvariable=var2)
var2.set("Creado y diseñado por Franco Calcia")
etiquetaAp.grid(column=2, row=7)

var3 = StringVar()
etiquetaAy = Label(root, textvariable=var3)
var3.set(" ")
etiquetaAy.grid(column=2, row=5)

# Crear barras de posición (escalas) para controlar los servos
angulo1 = Scale(root,
               command=servo1,
               from_=0,
               to=180,
               orient=HORIZONTAL,
               length=300,
               troughcolor='purple',
               width=30,
               cursor='dot',
               label='Posición Servo Base')
angulo1.grid(column=2, row=2)

angulo2 = Scale(root,
               command=servo2,
               from_=0,
               to=180,
               orient=HORIZONTAL,
               length=300,
               troughcolor='purple',
               width=30,
               cursor='dot',
               label='Posición Codo')
angulo2.grid(column=2, row=3)

angulo3 = Scale(root,
               command=servo3,
               from_=0,
               to=180,
               orient=HORIZONTAL,
               length=300,
               troughcolor='purple',
               width=30,
               cursor='dot',
               label='Posición Muñeca')
angulo3.grid(column=2, row=4)

angulo4 = Scale(root,
               command=servo4,
               from_=50,
               to=100,
               orient=HORIZONTAL,
               length=300,
               troughcolor='purple',
               width=30,
               cursor='dot',
               label='Posición Gripper')
angulo4.grid(column=2, row=5)

# Iniciar el bucle de eventos de la interfaz gráfica
root.mainloop()
