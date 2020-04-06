from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome("./drivers/chromedriver")
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
sleep(1)
a = driver.find_element_by_xpath("/html/body/table/tbody/tr/th")
b = driver.find_element_by_xpath("//tbody/tr/th")
d = driver.find_element_by_xpath("//th[text()='Savings']")
e = driver.find_element_by_xpath("//button[@id='clickOnMe']")
try:
    f = driver.find_element_by_xpath("//button[text()='Kliknij mnie!']")
except Exception as e:
    f = None
    print(e)
g = driver.find_element_by_xpath("//input[@id='fname']/following-sibling::table")
driver.close()
