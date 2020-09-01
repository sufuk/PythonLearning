from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9150)
binary = FirefoxBinary(r"C:\Tor Browser\Browser\firefox.exe")
driver = webdriver.Firefox(profile, binary)
driver.get("http://stackoverflow.com")
driver.save_screenshot("screenshot.png")
driver.quit()
