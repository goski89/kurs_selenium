import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")

# znajdz pole search
driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']").click()

# znajdz i wpisz London do inputa
search_input = driver.find_element_by_xpath("//div[@id='select2-drop']//div//input")
search_input.click()
search_input.send_keys('London')

# wybierz London z przeglądarki
find_result = driver.find_element_by_xpath("//div[@id='select2-drop']//ul//li//ul//li//div//span[text()='London']")
find_result.click()

# ustaw date zameldowania
check_in_date = driver.find_element_by_xpath("//div[@id='dpd1']").click()
find_in_month = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='next']")
find_current_month = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu']//div//table//thead//tr//th[@class='switch']")
while find_current_month.text != "July 2020":
    find_in_month.click()
find_in_day = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//tbody//tr//td[@class='day ' and text()='16']")
find_in_day.click()

# ustaw date wymeldowania
find_out_month = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='next']")
find_current_out_month = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='switch']")
while find_current_out_month.text != "September 2020":
    find_out_month.click()
find_out_day = driver.find_element_by_xpath("//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//tbody//tr//td[@class='day ' and text()='27']")
find_out_day.click()

# ustawienie ilości podrozujacych
find_traveller_input = driver.find_element_by_xpath("//input[@id='travellersInput' and @name='travellers']")
find_traveller_input.click()
adult_plus_btn = driver.find_element_by_id('adultPlusBtn')
adult_minus_btn = driver.find_element_by_id('adultMinusBtn')
child_plus_btn = driver.find_element_by_id('childPlusBtn')
child_minus_btn = driver.find_element_by_id('childMinusBtn')
child_input = driver.find_element_by_xpath("//input[@name='child']")

adult_plus_btn.click()
adult_plus_btn.click()
adult_minus_btn.click()

child_input.clear()
child_input.send_keys('3')
time.sleep(2)

# wyszukaj
search_btn = driver.find_element_by_xpath("//button[text()=' Search']")
search_btn.click()

# znajdz nazwy hoteli
hotels_list = driver.find_elements_by_xpath("//h4[@class='RTL go-text-right mt0 mb4 list_title']//b")
hotel_names = [hotel.get_attribute('textContent') for hotel in hotels_list]
print(hotel_names)
hotel_names = [hotel.__getattribute__('text') for hotel in hotels_list]
print(hotel_names)

# koniec
time.sleep(3)
driver.quit()
