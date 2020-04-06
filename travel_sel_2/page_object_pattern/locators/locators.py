class SearchHotelLocators:

    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//div[@id='select2-drop']//div//input"
    location_match_span_xpath = lambda city: f"//div[@id='select2-drop']//ul//li//ul//li//div//span[text()='{city}']"
    check_in_div_xpath = "//div[@id='dpd1']"
    date_picker_div_xpath = "//div[@class='datepicker dropdown-menu']"
    next_th_xpath = "//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='next']"
    current_month_th_xpath = "//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//thead//tr//th[@class='switch']"
    day_td_xpath = lambda check_in_day: f"//div[@class='datepicker dropdown-menu'][contains(@style, 'display: block')]//div//table//tbody//tr//td[@class='day ' and text()='{check_in_day}']"
    traveller_input_xpath = "//input[@id='travellersInput' and @name='travellers']"
    adult_input_xpath = "//input[@name='adults']"
    child_input_xpath = "//input[@name='child']"
    search_button_xpath = "//button[text()=' Search']"

class SearchResultsLocators:

    hotel_names_b_xpath = "//h4[@class='RTL go-text-right mt0 mb4 list_title']//b"
    hotel_prices_b_xpath = "//div[contains(@class, 'price_tab')]//b"