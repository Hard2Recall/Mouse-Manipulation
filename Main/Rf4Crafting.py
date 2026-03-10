from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #optional time.sleep(x) drzi klik x broj sekundi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



#runs untill 'q' key is pressed
while keyboard.is_pressed('q') == False:
    click(707, 807)
    time.sleep(1)
    