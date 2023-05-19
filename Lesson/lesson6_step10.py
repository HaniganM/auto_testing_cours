import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    #labels = browser.find_elements(by='tag name', value='label')
    #inputs = browser.find_elements(by='tag name', value='input')
    #for i, label in enumerate(labels):
    #    if label.text[-1] == '*':
    #        inputs[i].send_keys("blbblb")  этот код не выполняет задание

    input_name = browser.find_element(by='xpath', value='//input[@placeholder="Input your first name"]')
    input_name.send_keys('Ivan')
    input_familia = browser.find_element(by='xpath', value='//input[@placeholder="Input your last name"]')
    input_familia.send_keys('Petrov')
    input_mail = browser.find_element(by='xpath', value='//input[@placeholder="Input your email"]')
    input_mail.send_keys('blabla@bla')
    time.sleep(3)
    button = browser.find_element(by='css selector', value='button.btn')
    button.click()

    time.sleep(3)

    #находим элемент содержащий текст
    welcome_text_elt = browser.find_element(by='tag name', value='h1')

    #записсываем в переменную welcom_text текст из элемента welcom_text_elt
    welcome_text = welcome_text_elt.text

    #с помощью assert проверяем, что ожидаемый текст совподает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as error:
    print(f"ошибка - {error}")
finally:
    time.sleep(10)
    browser.quit()


