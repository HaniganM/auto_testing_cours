import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button1.click()
    time.sleep(5)

    new_window = browser.window_handles[
        1]  # берем вторую вкладку из возвращенного списка [0,1] и присваеваем переменной new_window
    browser.switch_to.window(new_window)  # переходим на вкладку new_window

    input1 = browser.find_element(By.ID, 'input_value')
    x_value = input1.text
    result = calc(x_value)

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(result)

    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()


except Exception as error:
    print(f'Ошибка - {error}')
finally:
    time.sleep(10)
    browser.quit()
