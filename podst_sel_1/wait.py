import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class WaitForListSize:
    def __init__(self, locator, ex_size):
        self.locator = locator
        self.ex_size = ex_size

    def __call__(self, driver):
        return len(driver.find_elements_by_xpath(self.locator)) == self.ex_size


start_time = time.time()

driver = webdriver.Chrome("./drivers/chromedriver")
wait = WebDriverWait(driver, 10, 0.5)
driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/waits2.html")

but = driver.find_element_by_id('clickOnMe').click()
# wait.until(lambda wd: len(wd.find_elements_by_tag_name("p")) == 2)
wait.until(WaitForListSize("//p", 1))
par = driver.find_element_by_tag_name('p')
print('udało się: ', par.text)

# try:
#     but = driver.find_element_by_id('clickOnMe').click()
#     par = driver.find_element_by_tag_name('p')
#     print('udało się: ', par.text)
# finally:
#     end_time = time.time()
#     print('czas: {:2f}'.format(end_time-start_time))

# count = 0
# while not par.is_displayed():
#     count += 1
#     if par.is_displayed():
#         print(par.is_displayed(), par.text)
#         break
#     else:
#         print(par.is_displayed(), par.get_attribute('textContent'))


# while not par.is_displayed():
#     print(f'stan: {par.is_displayed()}')
#     if par.is_displayed():
#         print(f'stan: {par.is_displayed()}')
#
#         break



# time.sleep(2)
# driver.quit()
