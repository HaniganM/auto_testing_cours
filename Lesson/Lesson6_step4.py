import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)
try:

    poisk_po_texty_ssilki = browser.find_element(by='link text', value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
    poisk_po_texty_ssilki.click()
    input1 = browser.find_element(by='tag name', value="input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value="last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value="form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id', value="country")
    input4.send_keys("Russia")
    button = browser.find_element(by="css selector", value="button.btn")
    button.click()
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла





