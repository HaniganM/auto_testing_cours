import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")


try:
    button = WebDriverWait(browser, 5).until(ES.element_to_be_clickable((By.ID, 'verify'))) # явное ожидание , гоаорим селениум, проверять в течении 5 секунд, пока кнопка не станет кликабельной
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
except Exception as error:
    print(f'{error}')
finally:
    time.sleep(3)
    browser.quit()
