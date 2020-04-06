from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

driver = webdriver.Chrome("./drivers/chromedriver")
# driver = webdriver.Chrome(ChromeDriverManager().install())

# # CLICK and ALERTS
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
sleep(1)
a = driver.find_element_by_xpath("//button[@id='clickOnMe']")
b = driver.find_element_by_xpath('//input[@id="fname"]')
c = driver.find_element_by_tag_name('select')
d = driver.find_element_by_xpath("//input[@type='checkbox']")
e = driver.find_element_by_xpath("//input[@value='male']")
f = driver.find_element_by_tag_name('p')
g = driver.find_element_by_class_name('topSecret')
h = driver.find_element_by_id("smileImage")
i = driver.find_element_by_id("newPage")

# f.get_attribute('textContent')
# g.get_attribute('textContent')
# print('{} \n{}'.format(f, g))

# e.click()
# d.click()
# a.click()
# sleep(1)
# driver.switch_to.alert.accept()
# sleep(1)
# a.click()
# sleep(1)
# driver.switch_to.alert.dismiss()
# sleep(1)
# b.send_keys('YOLO')
# sleep(1)
# a.send_keys(Keys.ENTER)
# sleep(1)
# auto_select = Select(c)
# auto_select.select_by_value('saab')
# sleep(1)
# auto_select.select_by_visible_text('Audi')
# sleep(1)
# auto_select.select_by_index(2)
# to_print = driver.find_element_by_id('fname').get_attribute('value')
# print('fname: {}'.format(to_print))

# h_size = h.size.get('height')
# h_size_nat = h.get_attribute('naturalHeight')
# print(f'h_size: {h_size}\nh_size_nat: {h_size_nat}')

# i.click()
# current_window = driver.current_window_handle
# windows_name = driver.window_handles
# for window in windows_name:
#     if window != current_window:
#         driver.switch_to.window(window)
# j = driver.find_element_by_name('q')
# j.send_keys('YOLO')
# j.send_keys(Keys.ENTER)
# driver.switch_to.window(current_window)


sleep(1)
driver.quit()
