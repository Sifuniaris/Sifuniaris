import pyautogui
import keyboard
from time import sleep

sleep(1)

while True:
    pyautogui.click()
    if keyboard.is_pressed("space"):
        break
