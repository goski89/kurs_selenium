import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
driver.maximize_window()

driver.execute_script("arguments[0].click();", driver.find_element_by_id('newPage'))
current_window = driver.current_window_handle
windows_name = driver.window_handles
for window in windows_name:
    if window != current_window:
        driver.switch_to.window(window)

temp = 'Dominik'
js_cmd = f"arguments[0].setAttribute('value', \'{temp}\')"
a = driver.find_element_by_name("q")
driver.execute_script(js_cmd, a)
a.send_keys(Keys.ENTER)

time.sleep(1)
driver.quit()
