import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_results import SearchResultPage

class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_cookie('ci_session')
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        search_hotel_page = SearchHotelPage(self.driver)
        self.driver.get(search_hotel_page.website)

        search_hotel_page.set_city('Dubai')
        search_hotel_page.set_date_range('2020', 'July', '12', True)
        search_hotel_page.set_date_range(2020, 'September', 20, False)
        search_hotel_page.set_travellers('2', 3)
        search_hotel_page.search()

        results_page = SearchResultPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        hotel_prices = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel", "zła nazwa hotelu 0"
        assert hotel_names[1] == "Oasis Beach Tower", "zła nazwa hotelu 1"
        assert hotel_prices[0] == "$22", "zła cena hotelu 0"
        assert hotel_prices[1] == "$50", "zła cena hotelu 1"
