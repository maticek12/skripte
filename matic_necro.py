from winreg import SaveKey
from pynput import mouse
from pynput.mouse import Button
from time import sleep
from secrets import randbelow
from datetime import datetime, timedelta

m = mouse.Controller()

def right_click():
    m.position = (798,386)
    m.click(Button.right)

def repair_all():
    m.position = (776,442)
    m.click(Button.left)

def click_again():
    m.position = (798,386)
    m.click(Button.left)

def select():
    m.position = (821,507)
    m.click(Button.left)

def start_ritual():
    m.position = (802,650)
    m.click(Button.left)
    
while True:
    right_click()
    sleep(3)
    repair_all()
    sleep(3)
    click_again()
    sleep(3)
    select()
    sleep(3)
    start_ritual()
    sleep(47)

