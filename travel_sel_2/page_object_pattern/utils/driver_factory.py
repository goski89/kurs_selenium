from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('start-maximize')
            options.set_capability("browserName", 'chrome')
            # return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            return webdriver.Remote("http://192.168.0.16:4444/wd/hub", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('start-maximize')
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        raise Exception('Provide valid driver name')
