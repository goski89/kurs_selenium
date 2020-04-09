from locators import locators
from selenium.webdriver.support.select import Select
import time
class BillingAddressUpdate:
    def __init__(self, driver):
        self.driver = driver

        self.reg_email_input = locators.BillingAddressLocators.reg_email_input
        self.reg_password_input = locators.BillingAddressLocators.reg_password_input
        self.register_btn = locators.BillingAddressLocators.register_btn
        self.addresses_link = locators.BillingAddressLocators.addresses_link
        self.edit_addresses_link = locators.BillingAddressLocators.edit_addresses_link

        self.first_name_input = locators.BillingAddressLocators.first_name_input
        self.last_name_input = locators.BillingAddressLocators.last_name_input
        self.company_input = locators.BillingAddressLocators.company_input
        self.country_select = locators.BillingAddressLocators.country_select
        self.address_1_input = locators.BillingAddressLocators.address_1_input
        self.address_2_input = locators.BillingAddressLocators.address_2_input
        self.postcode_input = locators.BillingAddressLocators.postcode_input
        self.city_input = locators.BillingAddressLocators.city_input
        self.phone_input = locators.BillingAddressLocators.phone_input
        self.email_input = locators.BillingAddressLocators.email_input

        self.save_address_btn = locators.BillingAddressLocators.save_address_btn

        self.msg_err = locators.BillingAddressLocators.msg_err
        self.msg_div = locators.BillingAddressLocators.msg_div

    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def set_company(self, company):
        self.driver.find_element(*self.company_input).send_keys(company)

    def edit_billing_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_addresses_link).click()

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)

    def set_address(self, street, postcode, city, optional=None):
        self.driver.find_element(*self.address_1_input).send_keys(street)
        if optional:
            self.driver.find_element(*self.address_2_input).send_keys(optional)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)

    def set_phone(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)

    def edit_email_address(self, email):
        self.driver.find_element(*self.email_input).clear()
        time.sleep(1)
        self.driver.find_element(*self.email_input).send_keys(email)

    def save_address(self):
        self.driver.find_element(*self.save_address_btn).click()

    def get_error_msg(self):
        return self.driver.find_element(*self.msg_div).text