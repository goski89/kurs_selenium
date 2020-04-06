import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("file:///home/dominik/workspace/kurs_selenium/podst_sel_1/demos/test.html")
    driver.maximize_window()
    yield
    driver.quit()


def test_title(test_setup):
    assert driver.title == "Strona testowa", f"Bad title: {driver.title}"


def test_title2(test_setup):
    assert driver.title == "Strona testowa", f"Bad title: {driver.title}"

