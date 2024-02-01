from pynput import keyboard
listening = False
control = keyboard.Controller()
def on_press(key):
     global listening
     if not listening and key == keyboard.Key.alt_gr:
          print("put on")
          listening = True
def on_release(key):
     control.type("teststr1")
     global listening
     if key == keyboard.Key.alt_gr:
          print("taken off")
          listening=False
with keyboard.Listener(on_press=on_press,on_release=on_release) as Listener:
     Listener.join()