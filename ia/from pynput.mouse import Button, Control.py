from pynput.mouse import Button, Controller
mouse = Controller()
print('The current pointer position is {0}'.format(
    mouse.position))