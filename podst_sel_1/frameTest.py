import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/testIframe.html")
driver.maximize_window()
a = driver.find_element_by_tag_name("h1")
print(a.text)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
b = driver.find_element_by_tag_name("h1")
print(b.text)
driver.switch_to.default_content()
c = driver.find_element_by_tag_name("h1")
print(c.text)

time.sleep(1)
driver.quit()
