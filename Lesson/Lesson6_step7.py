from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)
spisok = ["да", "нет", "Не знаю", "Конечно"]

try:
    elements = browser.find_elements(by='tag name', value="input")
    for element in elements:
        element.send_keys(random.choice(spisok))
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()
except Exception as error:
    print(f"Произошла ошибка , вот ее трейбек : {error}")
finally:
    time.sleep(20)
    browser.quit()
