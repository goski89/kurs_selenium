import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()

drag_source = driver.find_element_by_id('draggable')
drop_target = driver.find_element_by_id("droptarget")
webdriver.ActionChains(driver).drag_and_drop(drag_source, drop_target).perform()
time.sleep(5)
driver.quit()
