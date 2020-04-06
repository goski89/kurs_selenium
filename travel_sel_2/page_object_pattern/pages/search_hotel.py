from ..locators.locators import SearchHotelLocators as Locator
import logging
import allure

class SearchHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//div//input"
        self.location_match_span_xpath = lambda city: f"//div[@id='select2-drop']//ul//li//ul//li//div//span[text()='{city}']"

        self.check_in_div_xpath = "//div[@id='dpd1']"
        self.date_picker_div_xpath = "//div[@class='datepicker dropdown-menu']"
        self.next_th_xpath = "//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='next']"
        self.current_month_th_xpath = "//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='switch']"
        self.day_td_xpath = lambda check_in_day: f"//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//tbody//tr//td[@class='day ' and text()='{check_in_day}']"

        self.traveller_input_xpath = "//input[@id='travellersInput' and @name='travellers']"
        self.adult_input_xpath = "//input[@name='adults']"
        self.child_input_xpath = "//input[@name='child']"

        self.search_button_xpath = "//button[text()=' Search']"

    @allure.step("Setting city name to Dubai {1}")
    def set_city(self, city):
        self.logger.info(f"Setting city {city}")
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()

        search_input_obj = self.driver.find_element_by_xpath(self.search_hotel_input_xpath)
        search_input_obj.click()
        search_input_obj.send_keys(city)

        self.driver.find_element_by_xpath(self.location_match_span_xpath(city)).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=allure.attachment_type.PNG)

    @allure.step(f"Set check_{'in' if {4} else 'out'}_date: {3}/{2}/{1}")
    def set_date_range(self, year, month, day, click=False):
        self.logger.info(f'Ustaw check_{"in" if click else "out"}_date: {day}/{month}/{year}')
        if click:
            self.driver.find_element_by_xpath(self.check_in_div_xpath).click()

        next_btn_obj = self.driver.find_element_by_xpath(self.next_th_xpath)
        current_month_obj = self.driver.find_element_by_xpath(self.current_month_th_xpath)
        temp = f"{month} {str(year)}"
        while current_month_obj.text != temp:
            next_btn_obj.click()
        self.driver.find_element_by_xpath(self.day_td_xpath(str(day))).click()
        allure.attach(self.driver.get_screenshot_as_png(), name=f"set_date_check_{'in' if click else 'out'}", attachment_type=allure.attachment_type.PNG)


    @allure.step("Set Adult: {1} and Childrens: {2}")
    def set_travellers(self, adult, child):
        self.logger.info(f"Adults: {adult}, child: {child}")
        self.driver.find_element_by_xpath(self.traveller_input_xpath).click()

        adult_input_obj = self.driver.find_element_by_xpath(self.adult_input_xpath)
        child_input_obj = self.driver.find_element_by_xpath(self.child_input_xpath)

        adult_input_obj.click()
        adult_input_obj.clear()
        adult_input_obj.send_keys(str(adult))

        child_input_obj.click()
        child_input_obj.clear()
        child_input_obj.send_keys(str(child))
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travellers", attachment_type=allure.attachment_type.PNG)

    @allure.step("Click Search")
    def search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()