from selenium import webdriver
import time
import smtplib
import telegram
import os
from selenium.webdriver.chrome.options import Options

my_token = ''

def send(msg, chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)
chrome_options = Options()
chrome_options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
driver.get("https://web.whatsapp.com/")
a = input("Please switch the user u wanna check")
if a == "1":
    while a == "1":
        f = open(r"page_source.html", "w", encoding="utf-8")
        f.write(driver.page_source)
        f.close()
        file = open(r'page_source.html', "r", encoding="utf-8")
        if 'çevrimiçi' in file.read():
            message ="online"
            send(message, , token=my_token)
            time.sleep(20)
        file.close()
os.remove("page_source.html")
