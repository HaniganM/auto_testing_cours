import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num_1 = browser.find_element(By.ID, "num1")
    x = num_1.text
    num_2 = browser.find_element(By.ID, "num2")
    y = num_2.text
    result = int(x) + int(y)
    print(result)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(result))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f"ошибка - {error}")
finally:
    time.sleep(10)
    browser.quit()
