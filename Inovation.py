from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import random

keyboard = KeyboardController()
mouse = MouseController()

# Časovni sledilci
t_tipka_last = 0
l_miska_last = 0
l_miska_cooldown = 0

def check_and_activate(last_used_ref, activation_key, seconds_delay, hold_alt):
    global keyboard
    current_time = time.time()
    due_at = last_used_ref[0] + seconds_delay

    if current_time > due_at or last_used_ref[0] == 0:
        last_used_ref[0] = current_time
        if hold_alt:
            keyboard.press(Key.alt_l)

        keyboard.press(activation_key)
        keyboard.release(activation_key)

        if hold_alt:
            keyboard.release(Key.alt_l)

def check_and_press_random(last_used_ref, cooldown_ref, button, min_delay, max_delay):
    global mouse
    current_time = time.time()
    elapsed = current_time - last_used_ref[0]

    if elapsed > cooldown_ref[0] or last_used_ref[0] == 0:
        last_used_ref[0] = current_time
        cooldown_ref[0] = random.uniform(min_delay, max_delay)

        mouse.press(button)
        mouse.release(button)

# Uvodna zakasnitev (kot delay(10000) v Arduino)
print("Začetek čez 10 sekund...")
time.sleep(10)

# Zanki
tipka_tracker = [0]
miska_tracker = [0]
miska_cooldown = [0]

while True:
    check_and_activate(tipka_tracker, 't', 63, False)
    check_and_press_random(miska_tracker, miska_cooldown, Button.left, 65, 70)
    time.sleep(0.1)  # majhen delay za zmanjšanje obremenitve CPU
