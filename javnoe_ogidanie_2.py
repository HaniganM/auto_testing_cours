import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import math
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Firefox()
browser.get(link)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    button1 = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 10).until(ES.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button1.click()

    input1 = browser.find_element(By.ID, 'input_value')
    value = input1.text
    result = calc(value)

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(result)

    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

    alert_obj = browser.switch_to.alert
    msg = alert_obj.text
    print(msg)

except Exception as error:
    print(f'ошибка - {error}')
finally:
    time.sleep(15)
    browser.quit()

