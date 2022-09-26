import pyttsx3

temp = pyttsx3.init()
voice = temp.getProperty('voices')
temp.setProperty('voice',voice[1].id)
def speak(audio):
    print(audio)
    temp.say(audio)
    temp.runAndWait()
speak('Listening')