from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from time import sleep
from secrets import randbelow

sleep(5)

def rand_sleep(min: int, max: int):
    delta = max - min
    time = min + randbelow(delta)
    print(f"Sleeping for {time} ms")
    sleep(time / 1000)

    if randbelow(10) == 0:
        print(f"One in 10 extra")
        rand_sleep(60, 200)

    if randbelow(100) == 0:
        print(f"One in 100 extra")
        rand_sleep(400, 1000)

    if randbelow(1000) == 0:
        print(f"One in 1000 extra")
        rand_sleep(1400, 4000)

    return time

k = keyboard.Controller()
m = mouse.Controller()

for _ in range(40000):
    m.click(Button.left)
    rand_sleep(1201, 1700)
    k.tap("1")
    rand_sleep(1201, 1700)
    k.tap("1")
    rand_sleep(1201, 1700)
    k.tap(" ")
    rand_sleep(98_900, 99_300)
