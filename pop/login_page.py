import time

from selenium.webdriver.common.by import By

from features.common.base import Base
from utils.decrypt_utils import DecryptUtils
from utils.yaml_reader_utils import YamlReaderUtils


class LoginPage:
    username_txt = (By.CSS_SELECTOR, "#user")
    password_txt = (By.CSS_SELECTOR, "#password")
    login_with_atlassian_btn = (By.CSS_SELECTOR, "#login")
    login_btn = (By.CSS_SELECTOR, "#login-submit")

    def perform_login(self, context, username, password):
        """
        Function to handle login to the Application
        :param context: driver: browser instance
        :param username: YAML key
        :param password: YAML key
        """
        config = YamlReaderUtils.yaml_reader()
        context.driver.find_element(*self.username_txt).send_keys(config[username])
        context.driver.find_element(*self.login_with_atlassian_btn).click()
        # time.sleep(5)
        Base.wait_for_element_staleness(context, context.driver.find_element(*self.password_txt), 10)
        context.driver.find_element(*self.password_txt).send_keys(DecryptUtils.decrypter(config[password]))
        context.driver.find_element(*self.login_btn).click()

