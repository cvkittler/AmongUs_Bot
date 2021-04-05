import pyautogui
import time
import numpy as np
   
from check_keys import check_keyboard
import time
current_key = None
last_key = None

while True:
    current_key = check_keyboard()

    if(last_key == None):
        if(current_key == '='): #quit case
            break
        elif(current_key == ' '):
            curMousePos = pyautogui.position()
            print('Pos' + str(curMousePos))
            im = pyautogui.screenshot()
            img_rgb = np.array(im)
            print('R G B' + str(img_rgb[curMousePos[1]][curMousePos[0]]))

        last_key = current_key
    else:
        last_key = current_key

print('Qutting')