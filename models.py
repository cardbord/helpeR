import speech_recognition as sr
from pynput import keyboard
def on_press(key):
          global listening
          if not listening and key == keyboard.Key.alt_l:
               print("listening!")
               listening = True
               global stop
               
               stop = recog.listen_in_background(source,callback)

def on_release(key):
     if key == keyboard.Key.alt_l:
          global listening
          listening = False
          print("not listening!")
          stop(wait_for_stop=True)
  
class general:
     def __init__(self):
          self.listening = False
     
     





def callback(recognizer,audio):
     try:
          parseable = recognizer.recognize_whisper(audio,model="tiny")
          print(parseable)

     except sr.UnknownValueError:
          print("can't understand you!")
     except sr.RequestError as e:
          print(e)
     
recog = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
     recog.adjust_for_ambient_noise(source)




with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
     listener.join()