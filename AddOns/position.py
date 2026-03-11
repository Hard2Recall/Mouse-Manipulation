import pyautogui
import time
from PIL import ImageGrab
import keyboard  

#function that defines getting cursor cordinates and rgb color of the pixel that cursor is on
def get_mouse_position_and_color():
    x, y = pyautogui.position()
    image = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgb_color = image.getpixel((0, 0))
    return (x, y), rgb_color



#main function for starting the program
def main():
    print("Press ] to get mouse position and color. Press ESC to exit.")
    try:
        while True:
            #when ']' key is pressed get possition and RGB value
            if keyboard.is_pressed(']'):
                mouse_position, color = get_mouse_position_and_color()
                print(f"Mouse position: {mouse_position}, RGB color: {color}")
                time.sleep(0.3)  # Prevent multiple detections per press

            if keyboard.is_pressed('esc'): #stops the program when 'esc' is pressed
                print("\nProgram stopped.")
                break
    except KeyboardInterrupt:
        print("\nProgram interrupted.")     

if __name__ == "__main__":
    main()
