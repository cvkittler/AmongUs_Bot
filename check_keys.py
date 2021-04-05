import keyboard     # using module keyboard for getting keystokes

def check_keyboard():
    if keyboard.is_pressed(' '):  # if key 'q' is pressed 
        return " "
    elif keyboard.is_pressed('='): # if key 'p' is pressed
        return "="
    else:
        pass
