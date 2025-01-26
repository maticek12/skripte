from pynput import keyboard
from time import sleep
from secrets import randbelow
from datetime import datetime, timedelta

k = keyboard.Controller()
start = datetime.now()


class Timer:

    def __init__(self, name: str, key: str, interval_seconds: int):
        self.name = name
        self.key = key
        self.interval_seconds = interval_seconds
        self.last_used = datetime.now() - timedelta(
            seconds=self.interval_seconds)

    def activate(self):
        if datetime.now() > (self.last_used +
                             timedelta(seconds=self.interval_seconds)):
            print(f"Pressing {self.key} for {self.name} at {datetime.now()}")
            k.press(self.key)
            random_sleep(20, 50)
            k.release(self.key)
            self.last_used = datetime.now()
        else:
            print(f"Skipping {self.name} at {datetime.now()}")


def random_sleep(min_ms: int, max_ms: int):
    time_delta = max_ms - min_ms
    amount = min_ms + randbelow(time_delta)
    print(f"Sleeping for {amount} milliseconds")
    sleep(amount / 1000)


timers = [
    Timer("Looting", " ", 60),
    Timer("Overload", "7", 450),
    Timer("Penance powder", "8", 1760),
    Timer("Aggro pot", "9", 450),
    Timer("Incense sticks", "0", 550),
]

sleep(5)

while (start + timedelta(minutes=470)) > datetime.now():
    for timer in timers:
        timer.activate()
        random_sleep(1600, 2100)

    random_sleep(10_000, 30_000)
