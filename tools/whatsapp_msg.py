import pywhatkit as kit
import time
import datetime
import pyautogui

phone_num = str(input("Enter Mobile Number: "))
message = str(input("Enter Message: "))

current_time = datetime.datetime.now()
hour = current_time.hour
minutes = current_time.minute


kit.sendwhatmsg(phone_num, message, hour, minutes+2)
time.sleep(20)
pyautogui.press("Enter")



