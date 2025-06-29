from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from time import sleep
from secrets import randbelow

def rand_sleep(ms_min: int, ms_max: int):
    delta = ms_max - ms_min
    time = ms_min + randbelow(delta)
    print(f"Sleeping for {time} ms")
    sleep(time / 1000)
    return time

k = keyboard.Controller()
m = mouse.Controller()

# Počakamo 5 sekund pred začetkom
print("Začetek čez 5 sekund...")
sleep(5)

while True:
    # Levi klik
    m.click(Button.left)
    print("Klik miške")

    # Pavza med 1 in 2 sekundi
    rand_sleep(1000, 2000)

    # Pritisni SPACE
    k.tap(" ")
    print("Pritisnjen SPACE")

    # Pavza med 255 in 256 sekundami
    rand_sleep(255_000, 256_000)
