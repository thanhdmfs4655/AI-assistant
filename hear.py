from cgitb import text
from email.mime import audio
from sqlite3 import register_converter
import speech_recognition as sr
def hear():
    print('...')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print('I \n',end='')
        audio = r.listen(source,phrase_time_limit=3)
        try:
            text = r.recognize_google(audio,language='vi-VN')
            print(text)
            return str(text).lower()
        except:
            return None
        