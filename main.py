import pyautogui
from time import sleep
# from win32gui import GetWindowText, GetForegroundWindow
import tkinter as tk
import pygetwindow
import random
import keyboard

def prepare_minecraft():
    # set up window size and position, as well as the game object
    try:
        global game
        game = pygetwindow.getWindowsWithTitle('SkyClient (Forge 1.8.9)')[0]
        game.size = (870,590)
        game.moveTo(900,340)

    except pygetwindow.PyGetWindowException and IndexError:
        try:
            game = pygetwindow.getWindowsWithTitle('Minecraft 1.8.9')[0]
            game.size = (870,590)
            game.moveTo(900,340)

        except pygetwindow.PyGetWindowException and IndexError:
            print("Minecraft not found")
    return


def start():
    # focus setup
    try:
        global game
        pyautogui.moveTo(game.topleft[0] + game.size[0]/2, game.topleft[1] + game.size[1]/2)
        game.activate()
        
    except NameError:
        print("Minecraft not found")
        return
    
    fishes = 0 
    sleep(2)
    pyautogui.rightClick()
    
    # start fishing
    while keyboard.is_pressed('x') == False: 

        # active_window = GetWindowText(GetForegroundWindow())
        # if active_window == "Minecraft 1.8.9":
        #     pyautogui.rightClick()

        matching_color = pyautogui.pixelMatchesColor(930,397,(255, 85, 85))
        if matching_color == True:
            random_wait()
            pyautogui.rightClick()

            random_wait()
            pyautogui.rightClick()
            fishes += 1

        if fishes % 10 == 0 and fishes % 10 != 0:
            fishes_sleep = random.uniform(0.2,0.6)

            pyautogui.keyDown('a')
            sleep(fishes_sleep)
            pyautogui.keyUp('a')

            pyautogui.keyDown('d')
            sleep(fishes_sleep)
            pyautogui.keyUp('d')

    return


def random_wait():
    # random realistic wait time
    sleep(random.uniform(0.2, 0.5))
    return


# ui setup
root = tk.Tk()
root.title('Auto Fisher')
root.geometry('400x400')
root.resizable(False, False) 

title_text = tk.Label(root, text='Auto Fisher', font=('Arial', 20))
title_text.pack(side = 'top')

prepare_minecraft_button = tk.Button(root, text='Prepare Minecraft', command=prepare_minecraft)
prepare_minecraft_button.pack(side = 'top', pady = (25,0))

start_button = tk.Button(root, text='Start', command=start)
start_button.pack(side = 'top', pady = (25,0))

stop_button = tk.Label(root, text='Hold x for 2 seconds to stop', font=('Arial', 10))
stop_button.pack(side = 'top', pady = (25,0))

root.mainloop()