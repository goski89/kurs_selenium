from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.my_account_page import MyAccountPage
import pytest
import random
import time

@pytest.mark.usefixtures('setup')
class TestCreateAccount:


    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_my_account_page()
        my_account_page.create_account('dom.gorski@gmail.com', "Fibaro12345678")

        assert my_account_page.reg_msg_err in my_account_page.get_error_msg(), "Email address is already registered in service!"

    def test_create_account_passed(self):
        email = f"dom.gorski{random.randint(10, 10000)}@gmail.com"
        password = "Fibaro12345678"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_my_account_page()
        my_account_page.create_account(email, password)

        assert my_account_page.is_logout_link_displayed()