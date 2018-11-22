import pyautogui, time

currentX = 0
currentY = 0
lastX = 0
lastY = 0

while True:
    time.sleep(15)
    currentX, currentY = pyautogui.position()
    if currentX != lastX or currentY != lastY:
        lastX = currentX
        lastY = currentY
    else:
        pyautogui.moveRel(0,10)