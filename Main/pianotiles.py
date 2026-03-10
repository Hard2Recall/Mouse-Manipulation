from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#website that this exact code will work is: https://www.primarygames.com/arcade/music/pianotiles/

def Lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


#program will run until 'q' key is pressed
while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(992, 526)[0] == 0: #if pixel has value of red=0 click
        Lclick(992, 526)
    if pyautogui.pixel(773, 559)[0] == 0:
        Lclick(773, 559)
    if pyautogui.pixel(552, 564)[0] == 0:
        Lclick(552, 564)
    if pyautogui.pixel(334, 578)[0] == 0:
        Lclick(334, 578)