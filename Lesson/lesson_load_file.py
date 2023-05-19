import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Mamaev")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("JSKS@kcl")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к дериктории исполняемого скрипта
    file_path = os.path.join(current_dir, 'new_file.txt') # добовляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file') # находим элемент добовление файла
    element.send_keys(file_path) # добовляем файл

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f"ошибка - {error}")
finally:
    time.sleep(20)
    browser.quit()