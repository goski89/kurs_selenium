import pytest
import allure
import calendar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultPage
from page_object_pattern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures('setup')
class TestHotelSearch:

    @allure.title('This is title')
    @allure.description("test description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_hotel_search(self, data):
        search_hotel_page = SearchHotelPage(self.driver)
        self.driver.get("http://www.kurs-selenium.pl/demo")
        day = lambda x: x if x[0] != '0' else x[1]

        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range(data.check_in.split('/')[2], calendar.month_name[int(data.check_in.split('/')[1])], day(data.check_in.split('/')[0]), True)
        search_hotel_page.set_date_range(data.check_out.split('/')[2], calendar.month_name[int(data.check_out.split('/')[1])], day(data.check_out.split('/')[0]), False)
        search_hotel_page.set_travellers('2', 3)
        search_hotel_page.search()

        results_page = SearchResultPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        hotel_prices = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel", "zła nazwa hotelu 0"
        assert hotel_names[1] == "Oasis Beach Tower", "zła nazwa hotelu 1"
        assert hotel_prices[0] == "$22", "zła cena hotelu 0"
        assert hotel_prices[1] == "$50", "zła cena hotelu 1"
