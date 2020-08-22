from selenium import webdriver
import imagehash
from PIL import Image
import time
import winsound
import smtplib
import telegram
import os
driver = webdriver.Chrome()
url = "https://web.whatsapp.com/"
driver.get(url)
i = 1
time.sleep(20)
driver.save_screenshot(r"temp\tmp.png")
time.sleep(5)
shoot1 = Image.open(r"temp\tmp.png")
width, height = shoot1.size
left = 450
top = 10
right = 800
bottom = 70
shoot1_crop = shoot1.crop((left, top, right, bottom))
shoot1_crop.save(r"temp\ref.png")
os.remove(r"temp\tmp.png")
