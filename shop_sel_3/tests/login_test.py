from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage
import pytest

@pytest.mark.usefixtures('setup')
class TestLogIn:

    def test_log_in_fail(self):
        username = "dom.gorski@wp.com"
        password = "Fibaro12345678"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_my_account_page()
        my_account_page.log_in(username, password)

        assert my_account_page.login_msg_err in my_account_page.get_error_msg(), "Nie udana próba nieudanego logowania!"


    def test_log_in_passed(self, ):
        username = "dom.gorski@gmail.com"
        password = "Fibaro12345678"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_my_account_page()
        my_account_page.log_in(username, password)

        assert my_account_page.is_logout_link_displayed(), "Nie udana próba logowania!"
