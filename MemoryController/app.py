import psutil
import requests
import time

API_URL = "здесь будет урл апишки"
ALARM_THRESHOLD = 80

def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > ALARM_THRESHOLD:
        send_alarm()

def send_alarm():
    response = requests.post(API_URL)
    if response.status_code == 200:
        print("Alarm sent")
    else:
        print("Alarm error:", response.status_code)

while True:
    check_memory_usage()
    time.sleep(60)