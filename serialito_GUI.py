import tkinter as GUI
from tkinter import ttk  # Usar ttk para widgets con tema
from ttkthemes import ThemedTk
import serial
import time

# Crear la ventana con el tema "kroc"
window = ThemedTk(theme="blue")

# Variables globales
arduino = None  # No inicializar hasta que se seleccione el puerto

# Función para conectar con el microcontrolador

def CONECTAR():
    global arduino
    PUERTO = EntryCOM.get()  # Obtenemos el puerto ingresado
    try:
        arduino = serial.Serial(port=PUERTO, baudrate=115200, timeout=.1)
        print(f"Conectado a {PUERTO}")
    except Exception as e:
        print(f"Error al conectar: {e}")

# Función para enviar datos
def SEND():
    global arduino
    if arduino is not None and arduino.is_open:
        print("Enviando datos...")
        x = SpinDATA.get()  # Obtenemos el valor del Spinbox
        arduino.write(bytes(x, 'utf-8'))  # Enviamos el número en formato 'utf-8'
        time.sleep(0.05)  # Pausa breve
        data = arduino.readline().decode('utf-8').strip()  # Leemos la respuesta
        LabelRECIVE.config(text=f"Dato recibido = {data}")  # Mostramos el resultado
    else:
        LabelRECIVE.config(text="No conectado")

# Función para cerrar la conexión y la window
def CERRAR():
    global arduino
    if arduino is not None and arduino.is_open:
        arduino.close()  # Cerramos la conexión
        print("Conexión cerrada")
    window.destroy()  # Cerramos la window

# Creamos los widgets 
#en este  caso se usara ttk para que aparezcan el tema que elegimos (blue)
LabelCOM_NAME = ttk.Label(window, text="Escribe el nombre del puerto; ej: COM3")
EntryCOM = ttk.Entry(window)  # Campo de entrada sin valor predefinido
BotonCONECT = ttk.Button(window, text="CONECTAR", command=CONECTAR)
SpinDATA = ttk.Spinbox(window, from_=0, to=100)
BotonSEND = ttk.Button(window, text="ENVIAR", command=SEND)
LabelRECIVE = ttk.Label(window, text="Dato recibido = ")
BotonCerrar = ttk.Button(window, text="SALIR", command=CERRAR)

# Empaquetamos los widgets en la ventana

LabelCOM_NAME.pack(padx=1, pady=2)
EntryCOM.pack(padx=1, pady=2)
BotonCONECT.pack(padx=1, pady=2)
SpinDATA.pack(padx=1, pady=2)
BotonSEND.pack(padx=1, pady=2)
LabelRECIVE.pack(padx=1, pady=2)
BotonCerrar.pack(padx=1, pady=2)

# Iniciamos la ventana principal
window.mainloop()







