import pyautogui
import time
from PIL import ImageGrab
import keyboard  # Requires 'keyboard' module

def get_mouse_position_and_color():
    x, y = pyautogui.position()
    image = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgb_color = image.getpixel((0, 0))
    return (x, y), rgb_color

def main():
    print("Press ] to get mouse position and color. Press ESC to exit.")
    try:
        while True:
            if keyboard.is_pressed(']'):
                mouse_position, color = get_mouse_position_and_color()
                print(f"Mouse position: {mouse_position}, RGB color: {color}")
                time.sleep(0.3)  # Prevent multiple detections per press

            if keyboard.is_pressed('esc'):
                print("\nProgram stopped.")
                break
    except KeyboardInterrupt:
        print("\nProgram interrupted.")     

if __name__ == "__main__":
    main()
