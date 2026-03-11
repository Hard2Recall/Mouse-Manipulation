from pyautogui import *
import pyautogui
import time
import win32api, win32con



#website that this exact code will work is: https://humanbenchmark.com/tests/reactiontime

def Lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #optional time.sleep(x) drzi klik x broj sekundi
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

time.sleep(3) #delay so you can switch tabs


#main function
def doit():
    time.sleep(2)

    Lclick(1205, 391) #coordinates of the pixel that needs to be clicked

    while 1:
        if pyautogui.pixel(1172, 384) [1] == 219: #if pixel has value green=219 click
         click(1172, 384)
         break

#does doit function 5 times
for i in range (5):
   doit()