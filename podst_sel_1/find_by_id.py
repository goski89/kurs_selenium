from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome("./drivers/chromedriver")
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
sleep(1)
# driver.find_element_by_id("newPage").click()
# driver.find_element(By.ID, 'clickOnMe').click()
# driver.find_element_by_name('fname')
# driver.find_element_by_link_text("Visit W3Schools.com!")
# driver.find_element_by_partial_link_text("W3Schools.com!")
# driver.find_element_by_class_name("topSecret")
# driver.find_element_by_tag_name("a")
# driver.find_element_by_tag_name("div")
# driver.find_element_by_css_selector("img#smileImage")
a = driver.find_elements_by_css_selector("tr")
print(a)
driver.close()
