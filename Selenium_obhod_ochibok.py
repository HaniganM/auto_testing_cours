import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=chrome_options)
try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()