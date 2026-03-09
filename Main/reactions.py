from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



#https://humanbenchmark.com/tests/reactiontime

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #optional time.sleep(x) drzi klik x broj sekundi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3)

def doit():
    time.sleep(2)

    click(1205, 391)

    while 1:
        if pyautogui.pixel(1172, 384) [1] == 219:
         click(1172, 384)
         break

for i in range (5):
   doit()