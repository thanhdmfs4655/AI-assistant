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

#Weather API
apiKey = '7c72a8394be25515617c7cd571e7627e'
baseURL = 'https://api.openweathermap.org/data/2.5/weather?q='
cityName = 'hanoi'
completeURL = baseURL + cityName + '&appid=' + apiKey
response = requests.get(completeURL)
data = response.json()

class currentWeather():
    def currentTemperature(self):
        a = 'Current temperature is '
        b = a + str(data['main']['temp'])
        speak(b)
    def currentDiagnose(self):
        a = 'Current diagnose is '
        b = a + str(data['main']['feels_like'])
        speak(b)
    def temp_min():
        a = 'Today temp min is '
        b = a + str(data['main']['temp_min'])
        speak(b)
    def temp_max():
        a = 'Today temp max is '
        b = a + str(data['main']['temp_max'])
        speak(b)
    def humidity_now():
        a = 'Today humidity is '
        b = str(data['main']['humidity'])
        speak(b)
    def currentPressure():
        a = 'Current pressure is '
        b = a + str(data['main']['pressure'])
        speak(b)
    def sea_ground_level():
        a = 'Sea & ground level is '
        b = a + str(data['main']['sea_level']['grnd_level'])
        speak(b)
cW = currentWeather()


today = date.today()
class currentCalendar():
    def currentWeekday(self):
        today = datetime.now()
        weekday = date.weekday(today) + 2
        current_weekday = "Thu "+ str(weekday)
        if str(weekday) == '8':
            current_weekday = 'Chủ Nhật'
        a = 'Today is '
        b = a + current_weekday
        speak(b)
    def currentTime(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        a = "Current Time is "
        b = a + str(current_time)
        speak(b)
    def currentDate(self):
        today = date.today()
        nowday = today.strftime("%d")
        a = "Today is "
        b = a + str(nowday)
        speak(b)
    def currentMonth(self):
        month = today.strftime("%B")
        a = "Now is "
        b = a + str(month)
        speak(b)
    def currentYear(self):
        year = today.strftime("%Y")
        a = "Now is "
        b = a + str(year)
        speak(b)
cC = currentCalendar()

def AI_assistant():
    while True:
        you = hear()
        if you in 'Introduce yourself':
            speak("Hi, i'm cecil, i am your AI assistant!")
        elif you in "mấy giờ":
            cC.currentTime()
            continue
        elif you in "thứ mấy":
            cC.currentWeekday()
            continue
        elif you in "ngày bao nhiêu":
            cC.currentDate()
            continue
        elif you in "tháng mấy":
            cC.currentMonth()
            continue
        elif you in 'năm bao nhiêu':
            cC.currentYear()
        elif you in 'nhiệt độ bây giờ' or you in 'nhiệt độ':
            cW.currentTemperature()
        elif you in 'dự đoán thời tiết' or you in 'dự đoán':
            cW.currentDiagnose()
        elif you in 'nhiệt độ cao nhất':
            cW.temp_max()
        elif you in 'nhiệt độ thấp nhất':
            cW.temp_min()
        elif you in 'độ ẩm hiện tại' or you in 'độ ẩm':
            cW.humidity_now()
        elif you in 'áp lực hiện tại' or you in 'áp lực':
            cW.currentPressure()
        elif you in 'mật độ biển và đất' or you in 'biển và đất':
            cW.sea_ground_level()
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