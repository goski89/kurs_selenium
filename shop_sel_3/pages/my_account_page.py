from locators import locators

class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

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

    def open_my_account_page(self):
        self.driver.get(self.my_account_page)

    def log_in(self, username, password):
        self.driver.find_element(*self.login_username_input).send_keys(username)
        self.driver.find_element(*self.login_password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email).send_keys(email)
        self.driver.find_element(*self.reg_password).send_keys(password)
        self.driver.find_element(*self.reg_btn).click()

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.msg_err_xpath).text
