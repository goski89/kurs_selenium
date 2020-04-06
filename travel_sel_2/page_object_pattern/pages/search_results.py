from ..locators.locators import SearchResultsLocators as Locator
import logging
import allure


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Show list hotel")
    def get_hotel_names(self):
        hotels_list = self.driver.find_elements_by_xpath(Locator.hotel_names_b_xpath)
        hotel_names = [hotel.get_attribute('textContent') for hotel in hotels_list]
        for hotel in hotel_names:
            self.logger.info(f"Nazwa hotelu: {hotel}")
        allure.attach(self.driver.get_screenshot_as_png(), name="show_hotels_list", attachment_type=allure.attachment_type.PNG)
        return hotel_names

    @allure.step("Show hotel prices")
    def get_hotel_prices(self):
        prices_list = self.driver.find_elements_by_xpath(Locator.hotel_prices_b_xpath)
        hotel_prices = [price.get_attribute('textContent') for price in prices_list]

        return hotel_prices
