from check_keys import check_keyboard
from find_task import find_task
import time
current_key = None
last_key = None


while True:
    
    current_key = check_keyboard()

    if(last_key == None):
        if(current_key == '='): #quit case
            break
        elif(current_key == ' '):
            print('Space Bar has been detected')
            time.sleep(.3)
            find_task()
        last_key = current_key
    else:
        last_key = current_key
print('Qutting')