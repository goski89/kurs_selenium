import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
driver.maximize_window()

input_1 = driver.find_element_by_name("username")
input_1.clear()
input_1.send_keys('Dominik')

time.sleep(1)
driver.quit()
