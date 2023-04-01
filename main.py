# -*- coding: utf-8 -*-
import time

import keyboard


# When F7 is pressed, keep pressing E until F7 is pressed again.
if __name__ == "__main__":
    while True:
        keyboard.wait('F7')
        while True:
            keyboard.press('e')
            time.sleep(0.05)
            keyboard.release('e')
            time.sleep(0.05)
            if keyboard.is_pressed('F7'):
                break
