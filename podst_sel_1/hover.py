import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.w3schools.com")
driver.maximize_window()

button = driver.find_element_by_id('navbtn_references')

webdriver.ActionChains(driver).move_to_element(button).click(button).perform()
time.sleep(1)
driver.quit()
