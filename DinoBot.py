import time
from PIL import ImageGrab
import pyautogui


X = 470.0


def capture_image():
    img = ImageGrab.grab()
    return img


def detect_enemy(img):
    aux_color = img.getpixel((int(X), int(X + 60)))
    for x in range(int(X), int(X + 60)):
        for y in range(390, 413):
            color = img.getpixel((x, y))
            if color != aux_color:
                return True
            else:
                aux_color = color


def jump():
    global X
    pyautogui.press("up")
    X += 0.4


def crouch():
    pyautogui.press("down", 1, 0.1)


print("Start in 3 seconds...")
time.sleep(3)

while True:
    if detect_enemy(capture_image()):
        jump()
