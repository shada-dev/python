import pyautogui as auto
import time

msg = input("enter the message you want to send: ")
no_of_msg = int(input("how many messages you want to send: "))

time.sleep(10)
for i in range(no_of_msg):
	auto.write(msg)
	auto.press("Enter")				
	

