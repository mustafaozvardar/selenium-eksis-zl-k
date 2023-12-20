
from selenium import webdriver

from selenium.webdriver.common.by import By

import time 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome()
url="https://eksisozluk1999.com/mert-hakan-yandas--4637778?a=popular"
browser.get(url)
time.sleep(4)

elements = browser.find_elements(By.CSS_SELECTOR, ".content")
for element in elements:
    print("*********************************************************************************************")
    print(element.text)
browser.close()