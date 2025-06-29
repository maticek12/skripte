from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button
from time import sleep
from secrets import randbelow

# Počakaj 5 sekund preden začneš
sleep(5)

# Funkcija za naključno spanje (v milisekundah)
def nakljucno_spanje(min: int, max: int):
    razlika = max - min
    cas = min + randbelow(razlika)
    print(f"Spim {cas} ms")
    sleep(cas / 1000)

    # Dodatna naključna spanja
    if randbelow(10) == 0:
        print("1 proti 10 dodatno spanje")
        nakljucno_spanje(60, 200)

    if randbelow(100) == 0:
        print("1 proti 100 dodatno spanje")
        nakljucno_spanje(400, 1000)

    if randbelow(1000) == 0:
        print("1 proti 1000 dodatno spanje")
        nakljucno_spanje(1400, 4000)

    return cas

# Ustvari nadzor nad tipkovnico in miško
k = keyboard.Controller()
m = mouse.Controller()

# Neskončna zanka
while True:
    k.tap("1")  # pritisni tipko 1
    nakljucno_spanje(1201, 1700)
    k.tap(keyboard.Key.space)  # pritisni presledek (space)
    nakljucno_spanje(70900, 71300)  # počakaj ~71 sekund
