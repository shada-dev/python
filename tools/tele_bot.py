import requests
TOKEN = "6388115921:AAHRKbKKcuhXBkB1d48vnqowX44Q2t3Wb5o"
chat_id = "5661999583"
message = str(input("enter your msg here: "))
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)
