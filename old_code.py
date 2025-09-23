import pyautogui
import pygetwindow
import random
from time import sleep

def awooga():
    random_wait = random.uniform(0.1,0.3)
    sleep(random_wait)
    
sleep(2)

win = pygetwindow.getWindowsWithTitle('SkyClient (Forge 1.8.9)')[0]
win.size = (870, 519)

np = pyautogui.getActiveWindow()
np.moveTo(900, 340)

counter = 0
while True:
    counter += 1
    matching_color = pyautogui.pixelMatchesColor(930,397,(255, 85, 85))
    if matching_color == True:
        awooga()
        pyautogui.rightClick()
        print("awooga")
        awooga()
        pyautogui.rightClick()
    if counter % 20 == 0:
        random_wait = random.uniform(120,270)
        sleep(random_wait)
        pyautogui.press('a')
        random_wait = random.uniform(0.5,2)
        sleep(random_wait)
        pyautogui.press('d')
        print("moved")
