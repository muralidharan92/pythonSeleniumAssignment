from selenium import webdriver
from utils.yaml_reader_utils import YamlReaderUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:

    @staticmethod
    def open_and_launch_url_in_browser(browser):
        """
        Function to start instance of specified browser and navigate to the URL
        :param browser: name of the browser
        :return: driver: browser instance
        """
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
        else:
            raise Exception("The Browser type {} is not supported".format(browser))
        config = YamlReaderUtils.yaml_reader()
        url = config["url"].strip()
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def wait_for_element_present(context, locator, seconds=15):
        """
        Function to wait for element present
        :param context: driver: browser instance
        :param locator: By: locator
        :param seconds: time in seconds
        """
        wait = WebDriverWait(context.driver, int(seconds))
        wait.until(ec.presence_of_element_located(locator))

    @staticmethod
    def wait_for_element_staleness(context, locator, seconds=15):
        """
        Function to wait for element present
        :param context: driver: browser instance
        :param locator: By: locator
        :param seconds: time in seconds
        """
        wait = WebDriverWait(context.driver, int(seconds))
        wait.until(ec.staleness_of(locator))
