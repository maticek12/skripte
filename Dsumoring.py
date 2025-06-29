from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from time import sleep
from secrets import randbelow

running = True  # Globalna zastavica za ustavitev

def rand_sleep_ms(min_ms: int, max_ms: int):
    """Sleep za naključno količino milisekund."""
    delta = max_ms - min_ms
    time_ms = min_ms + randbelow(delta + 1)
    print(f"Spim {time_ms} ms")
    sleep(time_ms / 1000)
    return time_ms

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        print("ESC pritisnjen – ustavljam skripto.")
        running = False
        return False  # Ustavi listener

# Inicializacija
k = keyboard.Controller()
m = mouse.Controller()

# Čakaj pred začetkom
print("Čakam 7 sekund, nato zabeležim pozicijo miške... (ESC za ustavitev)")
sleep(7)

# Shrani začetno pozicijo miške
zapomni = m.position
print(f"Shranjena pozicija miške: {zapomni}")

# Zaženi tipkovnični listener v ozadju
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Glavna zanka
while running:
    m.position = zapomni
    m.click(Button.left)
    rand_sleep_ms(3000, 4000)

    k.tap(' ')
    rand_sleep_ms(2100, 2200)

    m.click(Button.left)
    rand_sleep_ms(2100, 2200)

    k.tap(' ')
    rand_sleep_ms(5000, 7000)

print("Skripta se je varno zaključila.")
