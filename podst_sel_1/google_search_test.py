from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome("./drivers/chromedriver")
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
sleep(2)
driver.quit()
