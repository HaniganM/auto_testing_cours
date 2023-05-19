from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Firefox()
browser.implicitly_wait(5)# искать каждый элемент в течении 5 секунд
browser.get(link)
try:
    button = browser.find_element(By.ID, 'verify')
    button.click()
    message = browser.find_element(By.ID, 'verify_message')

    assert 'successful' in message.text
except Exception as error:
    print(f'error - {error}')
finally:
    browser.quit()