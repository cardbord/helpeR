import speech_recognition as sr
import pyautogui
import time
from pynput import keyboard


listening = False
control = keyboard.Controller()
def on_press(key):
     global listening
     
     if key == keyboard.Key.f7:
          if not listening: 
               print("listening!")
               listening = True
               global stop
               
               stop = recog.listen_in_background(source,callback_google)
     

def on_release(key):
     if key == keyboard.Key.f7:
          global listening
          
          listening = False
          print("not listening!")
          stop()

def callback_whisper(recognizer,audio):
     try:
          parseable = recognizer.recognize_whisper(audio,model="tiny")
          print(parseable)

     except sr.UnknownValueError:
          print("can't understand you!")
     except sr.RequestError as e:
          print(e)

def callback_google(recognizer,audio):
     try:
          parseable:str = recognizer.recognize_google(audio) #no params here
          print(parseable)

          #HASHTAG IF UNWANTED
          
          parseable=parseable.replace("open bracket", "(").replace("close bracket",")").replace("colon",':').replace("comma",',').replace("open list",'[').replace("close list",']').replace("open dictionary","{").replace("close dictionary","}").replace("multiply",'*').replace("divide","/").replace("mod",'%').replace("div",'//').replace("open speech",'"').replace("close speech",'"').replace("comment",'#').replace("dot", ".")
          for word in parseable.split(' '):
               space_at_the_end = True
               match word:
                    case "enter":
                         space_at_the_end = False
                         control.tap(keyboard.Key.enter)
                    case "escape":
                         control.tap(keyboard.Key.esc)
                    case "delete":
                         control.press(keyboard.Key.shift_l)
                         control.press(keyboard.Key.end)
                         control.release(keyboard.Key.end)
                         control.release(keyboard.Key.shift_l)
                         control.tap(keyboard.Key.delete)
                    case "tab":
                         control.tap(keyboard.Key.tab)
                    case _:
                         if word in ["(",")",'"',"{","}","[","]",".","#"]:
                              space_at_the_end = False
                         control.type((word+" ") if space_at_the_end else word)
                         print(word)



     
     
     
     except sr.UnknownValueError:
          print("can't understand you!")
     except sr.RequestError as e:
          print(e)

def callback_sphinx(recognizer,audio):
     try:
          parseable = recognizer.recognize_sphinx(audio)
          print(parseable)
          

     except sr.UnknownValueError:
          print("can't understand you!")
     except sr.RequestError as e:
          print(e)

def callback_vosk(recognizer,audio):
     try:
          parseable = recognizer.recognize_vosk(audio)
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