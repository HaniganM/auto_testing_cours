import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_index("3")# выбор по индексу, индексация начинается с нуля
    #select.select_by_value("1") -- по значению Value
    #select.select_by_visible_text() -- по тексту

finally:
    time.sleep(10)
    browser.quit()
