import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/doubleClick.html")
driver.maximize_window()

button = driver.find_element_by_id('bottom')
webdriver.ActionChains(driver).context_click(button).perform()

time.sleep(1)
driver.quit()
