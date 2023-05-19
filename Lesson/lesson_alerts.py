import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
    time.sleep(3)

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    result = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(result)

    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

except Exception as error:
    print(f'ошибка - {error}')
finally:
    time.sleep(10)
    browser.quit()