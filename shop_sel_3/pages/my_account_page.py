from locators import locators
import logging
import allure

class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.my_account_link = locators.MyAccountPage.my_account_link
        self.my_account_page = locators.MyAccountPage.my_account_page

        self.login_username_input = locators.MyAccountPage.login_username_input
        self.login_password_input = locators.MyAccountPage.login_password_input
        self.login_btn = locators.MyAccountPage.login_btn
        self.login_msg_err = locators.MyAccountPage.login_msg_err

        self.reg_email = locators.MyAccountPage.reg_email_input
        self.reg_password = locators.MyAccountPage.reg_password_input
        self.reg_btn = locators.MyAccountPage.reg_btn
        self.reg_msg_err = locators.MyAccountPage.reg_msg_err

        self.msg_err_xpath = locators.MyAccountPage.msg_err_xpath
        self.logout_link = locators.MyAccountPage.logout_link

    @allure.step("Open page with account info")
    def open_my_account_page(self):
        self.logger.info(f"Open page: '{self.my_account_page}'")
        self.driver.get(self.my_account_page)

    @allure.step("Login")
    def log_in(self, username, password):
        self.logger.info(f"Set username: {username}, password: {password}")
        self.driver.find_element(*self.login_username_input).send_keys(username)
        self.driver.find_element(*self.login_password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    @allure.step("Create account")
    def create_account(self, email, password):
        self.logger.info(f"Create account with email: {email}, password: {password}")
        self.driver.find_element(*self.reg_email).send_keys(email)
        self.driver.find_element(*self.reg_password).send_keys(password)
        self.driver.find_element(*self.reg_btn).click()

    @allure.step("Is logout link dispplayed")
    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    @allure.step("Get error msg")
    def get_error_msg(self):
        temp = self.driver.find_element(*self.msg_err_xpath).text
        self.logger.info(f"MSG: {temp}")
        return temp
