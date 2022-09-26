from re import sub
from hear import *
from speak import *
import webbrowser
from datetime import date
from datetime import datetime
from datetime import date
import subprocess
def currentTime():
    today = datetime.now()
    weekday = date.weekday(today) + 2
    current_weekday = "Thu "+ str(weekday)
    if str(weekday) == '8':
        current_weekday = 'Chủ Nhật'
    print(current_weekday)
while True:
    you = hear()
    if you in "mấy giờ":
        speak('9 oclock')
        continue
    elif you in "thứ mấy":
        speak(currentTime())
        continue
    elif you in "ngày bao nhiêu":
        speak('24')
        continue
    elif you in "tháng mấy":
        speak('September')
        continue
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