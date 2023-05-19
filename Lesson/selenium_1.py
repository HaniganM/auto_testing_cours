import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)
time.sleep(5)

driver.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(5)
driver.quit()
