import pyautogui as gui, sys

print('Press Ctrl + C to quit.')
try:
    while True:
        x, y = gui.position()
        pos = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(pos, end = '')
        print('\b' * len(pos), end = '', flush = False)
except KeyboardInterrupt:
    print('\n')
    gui.moveTo(1375, 65, 2)
    gui.click()
    gui.click()