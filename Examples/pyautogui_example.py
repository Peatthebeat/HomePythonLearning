#! python3
# puautogui_example.py - Program that demonstrate the capability of GUI automation through keyboard and mouse automation

import pyautogui
import time
import sys

# pyautogui.PAUSE = 1         # will pause every command for a second
pyautogui.FAILSAFE = True   # will have a failsafe disable.  Move top-left mouse to raise an pyautogui.FailSafeException

''' For mouse movements:
                        top-left is 0,0
                        top-right is 1919,0
                        bottom-left is 0,1079
                        bottom-right is 1919,1079'''

''''width, height = pyautogui.size()
print(width)
print(heigh)'''

# for absolute mouse movement
def absolute():
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

# for relative mouse movement
def relative():
    for i in range(10):
        pyautogui.moveRel(100, 0, pyautogui.easeOutQuad, duration=0.25)
        pyautogui.moveRel(0, 100, duration=0.25)
        pyautogui.moveRel(1919, 1079, duration=0.25)
        pyautogui.moveRel(-100, 0, duration=0.25)
        pyautogui.moveRel(0, -100, duration=0.25)
        pyautogui.moveRel(0, 0, duration=2)

''' # Mouse position
MouseX, MouseY = pyautogui.position()
print('Mouse is @ X: ' + str(MouseX) + ' & Y: ' + str(MouseY))'''


'''pyautogui.moveTo(0, 1079, duration=0.5)
pyautogui.click()
pyautogui()
time.sleep(5)
pyautogui.rightClick()'''

def displaypos():
    print('Press CTRL-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
            print(positionStr, end='')
            time.sleep(1)
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nDone.')

# You can have the program recognize part of the program and let it click it
def imagerecognition():
    clickreviewexcel = pyautogui.locateOnScreen('review.png')
    print(clickreviewexcel)
    if clickreviewexcel is not None:
        pyautogui.click(pyautogui.center(clickreviewexcel))
    else:
        print('review not found')

# this section is to display stuff while using the script
pyautogui.alert('This displays an alert')
ask = pyautogui.confirm('This is to confirm')
if ask == 'OK':
    print('OK was pressed')
else:
    print('Cancel was pressed')
pyautogui.password('Please Enter Password:', mask='*')


inputfromUser = (pyautogui.prompt('This let\'s users input a text'))
print(inputfromUser)

# relative()
# absolute()
# displaypos()
# imagerecognition()



