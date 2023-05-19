import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element(By.ID, "treasure")
    x_valuex = x_element.get_attribute("valuex")
    x = x_valuex
    result = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    input4 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input4.click()

except Exception as error:
    print(f"ошибка - {error}")
finally:
    time.sleep(20)
    browser.quit()
