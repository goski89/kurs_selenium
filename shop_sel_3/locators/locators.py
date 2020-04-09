from selenium.webdriver.common.by import By


class BillingAddressLocators:

    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    register_btn = (By.NAME, 'register')
    addresses_link = (By.LINK_TEXT, 'Addresses')
    edit_addresses_link = (By.XPATH, "//a[contains(@href, 'edit-address=billing')]")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    company_input = (By.ID, "billing_company")
    country_select = (By.ID, "billing_country")
    address_1_input = (By.ID, "billing_address_1")
    address_2_input = (By.ID, "billing_address_2")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    email_input = (By.ID, "billing_email")
    save_address_btn = (By.XPATH, '//button[@name="save_address" and text()="Save address"]')
    msg_err = "Address changed successfully."
    msg_div = (By.XPATH, "//div[@class='woocommerce-message']")


class MyAccountPage:

    my_account_link = (By.XPATH, "//li[@id='menu-item-22']//a")
    my_account_page = "http://www.seleniumdemo.com/?page_id=7"

    login_username_input = (By.ID, "username")
    login_password_input = (By.ID, "password")
    login_btn = (By.NAME, "login")
    login_msg_err = "Incorrect username or password"

    reg_email_input = (By.ID, 'reg_email')
    reg_password_input = (By.ID, 'reg_password')
    reg_btn = (By.NAME, 'register')
    reg_msg_err = "An account is already registered with your email address. Please log in."

    msg_err_xpath = (By.XPATH, "//ul[@class='woocommerce-error']//li")

    logout_link = (By.LINK_TEXT, "Logout")

