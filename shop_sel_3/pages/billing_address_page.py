from locators import locators
from selenium.webdriver.support.select import Select
import time
import allure
import logging

class BillingAddressUpdate:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

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

    @allure.step("Set firstname and lastname")
    def set_personal_data(self, first_name, last_name):
        self.logger.info(f"Set fistname: {first_name}, lastname: {last_name}")
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Set Company name")
    def set_company(self, company):
        self.logger.info(f"Set company: {company}")
        self.driver.find_element(*self.company_input).send_keys(company)
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Click billing address edit")
    def edit_billing_address(self):
        self.logger.info(f"Click address section and next click edit link")
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_addresses_link).click()
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Set Country")
    def select_country(self, country):
        self.logger.info(f"Set country '{country}' in select object")
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Set Address")
    def set_address(self, street, postcode, city, optional=None):
        self.logger.info(f"Set adress with street: '{street}', postcode: '{postcode}', city: '{city}'")
        self.driver.find_element(*self.address_1_input).send_keys(street)
        if optional:
            self.driver.find_element(*self.address_2_input).send_keys(optional)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Set phone number")
    def set_phone(self, number):
        self.logger.info(f"Set phone number to: '{number}'.")

        self.driver.find_element(*self.phone_input).send_keys(number)

        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Edit Email adress")
    def edit_email_address(self, email):
        self.logger.info(f"Change email to {email}")

        self.driver.find_element(*self.email_input).clear()
        time.sleep(1)
        self.driver.find_element(*self.email_input).send_keys(email)

        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)

    @allure.step("Click SAVE button")
    def save_address(self):
        self.logger.info(f"Click Save button")

        self.driver.find_element(*self.save_address_btn).click()

    @allure.step("Get msg after actions")
    def get_error_msg(self):
        self.logger.info(f"Check response msg.")

        temp = self.driver.find_element(*self.msg_div).text
        allure.attach(self.driver.get_screenshot_as_png(), name=__name__, attachment_type=allure.attachment_type.PNG)
        return temp