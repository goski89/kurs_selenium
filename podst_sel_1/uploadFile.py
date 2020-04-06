import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome("./drivers/chromedriver")
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/uploadFile.html")
driver.maximize_window()

input_file = driver.find_element_by_xpath("//input[@type='file']")
screen_path = os.path.abspath("screenschoots")
file_path = os.path.abspath("demos/smile.png")
print(file_path)
driver.get_screenshot_as_file(f"{screen_path}/{time.time()}.png")

input_file.send_keys(file_path)
driver.get_screenshot_as_file(f"{screen_path}/{time.time()}.png")
time.sleep(2)
driver.quit()
