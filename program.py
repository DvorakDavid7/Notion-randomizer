from pynput.keyboard import Key, Controller
import time
import random


keyboard = Controller()
DELAY = 0.1

def press_once(key):
    keyboard.press(key)
    keyboard.release(key)

def moveUp(n):
    keyboard.press(Key.shift_l)
    keyboard.press(Key.ctrl_l)
    for i in range(n):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(DELAY)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift_l)

def goUp(n):
    for i in range(n):
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(DELAY)

def goDown(n):
    for i in range(n):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(DELAY)

def moveDown(n):
    keyboard.press(Key.shift_l)
    keyboard.press(Key.ctrl_l)
    for i in range(n):
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        time.sleep(DELAY)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.shift_l)


def main():
    try:
        toggles = int(input("How many toggles do you have? "))
    except Exception:
        print("Invalid input")
        return False
    print("Click on the first one!")
    time.sleep(5)
    press_once(Key.esc)
    time.sleep(0.5)
    rand = random.randint(1, toggles - 1)
    for _ in range(toggles * 2):
        moveDown(rand)
        goUp(rand)
        rand = random.randint(1, toggles - 1)
    

if __name__ == "__main__":
    main()