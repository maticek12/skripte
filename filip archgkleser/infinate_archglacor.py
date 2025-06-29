from time import sleep
import pynput.mouse as mouse
import pynput.keyboard as keyboard
from threading import Thread
from datetime import datetime
from secrets import randbelow

k = keyboard.Controller()
m = mouse.Controller()

key_teleport="8"
key_surge="t"
location_hub_portal=(673,145)
location_aqueduct_portal=(916,27)
location_start_button=(1163,719)
compass=(1354,78)

sleep(5)

def click_at(coordinates: tuple[int,int]):
    m.position = coordinates
    m.click(mouse.Button.left)

def prevent_lobby():
    while True:
        random_milliseconds = randbelow(100_000)
        print(f"Sleeping for {random_milliseconds} milliseconds.")
        sleep(random_milliseconds / 1_000)
        print(f"{datetime.now()}: Preventing lobby")
        k.tap(" ")
        

Thread(target=prevent_lobby).start()

while True:
    k.tap(key_teleport)
    sleep(10)
    click_at(compass)
    k.tap(key_surge)
    sleep(2)
    click_at(location_hub_portal)
    sleep(12)
    click_at(location_aqueduct_portal)
    sleep(6)
    click_at(location_start_button)
    sleep(5)
    k.tap(key_surge)
    sleep(120)
    click_at((1163,719))
    sleep(3500)
    