import time
import pyautogui
from sys import exit
import keyboard

while True:
    try:
        pyautogui.click(1671, 1008)
        
        for s in range(660):
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
                print("Programa cerrado")
                exit(0)
            time.sleep(1)
        
    except KeyboardInterrupt:
        print("Programa cancelado")
        exit(0)

