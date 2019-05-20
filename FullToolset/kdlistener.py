
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print key.char.encode("ascii"),
    except AttributeError:
        print str(key)
        
def on_release(key):
    try:
        if (key == key.esc):
            return False
    except:
        pass

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
