import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed !=before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="ss_if_failed", attachment_type=allure.attachment_type.PNG)
    driver.quit()
