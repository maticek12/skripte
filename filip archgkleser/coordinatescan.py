from pynput.mouse import Controller
from pynput.keyboard import Listener as K, Key, KeyCode

m = Controller()

def handler(key: KeyCode):
    try:
        if key == Key.esc:
            print(f"{m.position}")
    except:
        pass

listener = K(on_release=handler)

listener.start()
listener.join()