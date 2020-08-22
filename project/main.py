from selenium import webdriver
import imagehash
from PIL import Image
import time
import winsound
import smtplib
import telegram
my_token = ''

def send(msg, chat_id, token=my_token):
	bot = telegram.Bot(token=token)
	bot.sendMessage(chat_id=chat_id, text=msg)
driver = webdriver.Chrome()

url = "https://web.whatsapp.com/"
driver.get(url)
i = 1
time.sleep(20)
while i == 1:
    driver.save_screenshot("temp\shoot1.png")
    time.sleep(5)
    driver.save_screenshot("temp\shoot2.png")
    shoot1 = Image.open("temp\shoot1.png")
    width, height = shoot1.size
    left = 450
    top = 10
    right = 800
    bottom = 70
    shoot1_crop = shoot1.crop((left, top, right, bottom))
    shoot1_crop.save("temp\shoot1_crop.png")
    shoot2 = Image.open("temp\shoot2.png")
    width, height = shoot2.size
    shoot2_crop = shoot2.crop((left, top, right, bottom))
    shoot2_crop.save("temp\shoot2_crop.png")
    hash = imagehash.average_hash(Image.open('temp\shoot1_crop.png'))
    otherhash = imagehash.average_hash(Image.open('temp\shoot2_crop.png'))
    a = hash - otherhash
    hash2 = imagehash.average_hash(Image.open('temp\shoot1_crop.png'))
    otherhash2 = imagehash.average_hash(Image.open(r'temp\abs.png'))
    b = hash2 - otherhash2
    hash3 = imagehash.average_hash(Image.open('temp\shoot2_crop.png'))
    otherhash3 = imagehash.average_hash(Image.open(r'temp\abs.png'))
    c = hash3 - otherhash3
    j = 0
    if a != 0:
        j = 1
    if b != 0:
        j = 1
    if c != 0:
        j = 1
    if j == 1:
        message ="cigdem online"
        send(message, , token=my_token)
