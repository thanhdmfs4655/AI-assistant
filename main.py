from calendar import month
from re import T, sub
from ssl import VERIFY_X509_TRUSTED_FIRST
from urllib import response
from hear import *
from speak import *
import webbrowser
from datetime import date
from datetime import datetime
from datetime import date
import requests, json
import subprocess
apiKey = '7c72a8394be25515617c7cd571e7627e'
baseURL = 'https://api.openweathermap.org/data/2.5/weather?q='
cityName = input('Enter your city : ')
completeURL = baseURL + cityName + '&appid=' + apiKey
response = requests.get(completeURL)
data = response.json()
today = date.today()
def currentWeekday():
    today = datetime.now()
    weekday = date.weekday(today) + 2
    current_weekday = "Thu "+ str(weekday)
    if str(weekday) == '8':
        current_weekday = 'Chủ Nhật'
    print(current_weekday)
def currentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
def currentDate():
    today = date.today()
    nowday = today.strftime("%d")
    print("Today is", nowday)
def currentMonth():
    month = today.strftime("%B")
    print("Now is", month)
def currentTemperature():
    print('Current temperature is',data['main']['temp'])
def currentDiagnose():
    print('Current diagnose is',data['main']['feels_like'])
def temp_min():
    print('Today temp min is',data['main']['temp_min'])
def temp_max():
    print('Today temp max is',data['main']['temp_max'])
def humidity_now():
    print('Today humidity is',data['main']['humidity'])
def currentPressure():
    print('Current pressure is',data['main']['pressure'])
def sea_ground_level():
    print('Sea & ground level is',data['main']['sea_level']['grnd_level'])

def AI_assistant():
    while True:
        you = hear()
        if you in "mấy giờ":
            speak(currentTime())
            continue
        elif you in "thứ mấy":
            speak(currentWeekday())
            continue
        elif you in "ngày bao nhiêu":
            speak(currentDate())
            continue
        elif you in "tháng mấy":
            speak(currentMonth())
            continue
        elif you in 'nhiệt độ bây giờ':
            speak(currentTemperature())
        elif you in "Stop":
            break
        elif you in 'open facebook':
            webbrowser.open('https://www.facebook.com/')
            continue
        elif you in 'microsoft edge':
            subprocess.Popen('"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"')
            continue
        elif you in 'open zalo':
            subprocess.Popen(r'C:\Users\minht\AppData\Local\Programs\Zalo\Zalo.exe')
            continue
        elif you in 'open google':
            webbrowser.open('https://www.google.gg/')
            continue
        elif you in 'open youtube':
            webbrowser.open('https://www.youtube.com/?gl=VN')
            continue
        elif you in 'open garena':
            subprocess.Popen('"C:\Program Files (x86)\Garena\Garena\Garena.exe"')
            continue
        elif you in 'open notion':
            subprocess.Popen(r'C:\Users\minht\AppData\Local\Programs\Notion\Notion.exe')
            continue
        elif you in 'open steam':
            subprocess.Popen('"C:\Program Files (x86)\Steam\steam.exe"')
            continue
        else:
            speak("I can't hear that !")
AI_assistant()