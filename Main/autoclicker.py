from pyautogui import *
import time
import keyboard
import win32api, win32con


#look in paste.py for explanation
def Lclick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #optional time.sleep(x) hold click x amount of seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



#program will run untill 'q' key is pressed
while keyboard.is_pressed('q') == False:
    Lclick(769, 400) #coordinates of the pixel that needs to be clicked
    time.sleep(0.2)
    