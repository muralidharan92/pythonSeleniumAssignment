from selenium.webdriver.common.by import By
from features.common.base import Base


class HomePage:
    def click_board_tile(self, context, tile_name):
        """
        Function to click board tile based on parameter
        :param context: driver: Browser instance
        :param tile_name: Board tile name
        """
        Base.wait_for_element_present(context, (By.XPATH, "//li//*[text()='{}']".format(tile_name)), 10)
        context.driver.find_element_by_xpath("//li//*[text()='{}']".format(tile_name)).click()
