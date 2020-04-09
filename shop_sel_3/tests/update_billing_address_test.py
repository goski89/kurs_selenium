from pages.my_account_page import MyAccountPage
from pages.billing_address_page import BillingAddressUpdate
import pytest
import random
import allure

@pytest.mark.usefixtures('setup')
class TestUpdateBillingAddress:

    @allure.title("Test uzupełnienia danych")
    @allure.description("uzupelniamy dane do platnosci")
    def test_update_billing(self):
        email = f"dom.gorski{random.randint(10, 10000)}@gmail.com"
        password = "Fibaro12345678"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_my_account_page()
        my_account_page.create_account(email, password)

        billing_address_page = BillingAddressUpdate(self.driver)
        billing_address_page.edit_billing_address()
        billing_address_page.set_personal_data('Dominik', 'Górski')
        billing_address_page.set_company('Fibaro')
        billing_address_page.select_country('Poland')
        billing_address_page.set_address('Serdeczna 1', '62-000', "Wysogotowo", "Chujowa firma")
        billing_address_page.set_phone('666666666')
        billing_address_page.edit_email_address('stoper@wp.pl')
        billing_address_page.save_address()

        assert billing_address_page.msg_err in billing_address_page.get_error_msg(), 'Nieudana próba edycji danych!'



