import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("./drivers/chromedriver")
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
driver.maximize_window()

# input_fname = driver.find_element_by_name("fname")
# secret = driver.find_element_by_class_name('topSecret')
# if secret.is_displayed():
#     print('not secret!')
#     print(secret.text)
# else:
#     print('top secret!')
#     print(secret.get_attribute('textContent'))

# checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
# checkbox.click()
# print(checkbox.is_selected())

time.sleep(2)
driver.quit()
