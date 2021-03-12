from selenium.webdriver.common.by import By
from datetime import datetime

from features.common.base import Base


class AddBoardPage:
    add_board_title_txt = (By.CSS_SELECTOR, "input[data-test-id='create-board-title-input']")
    visibility_dropdown_btn = (By.CSS_SELECTOR, "._1Lkx3EjS3wCrs7.voB8NatlbuEme5._3JfnLi33JtGtIk")
    create_board_btn = (By.CSS_SELECTOR, "button[data-test-id='create-board-submit-button']")
    yes_make_board_public_btn = (By.CSS_SELECTOR, ".voB8NatlbuEme5._21upOlzpUQJcdT.gkv95EhjCrfcEU")
    board_name_title_lbl = (By.CSS_SELECTOR, ".js-board-editing-target.board-header-btn-text")

    def add_board(self, context, visibility):
        """
        Function to add board and handle visibility based on parameter
        :param context: driver: Browser instance
        :param visibility: visibility options ["Public", "Private", "Team Visible"]
        """
        time_stamp = datetime.now().strftime("%b-%d-%Y-%H%M%S")
        context.driver.find_element(*self.add_board_title_txt).send_keys("test-board-{}".format(time_stamp))
        current_visibility = context.driver.find_element(*self.visibility_dropdown_btn).text
        if current_visibility not in visibility:
            context.driver.find_element(*self.visibility_dropdown_btn).click()
            if visibility == "Private":
                context.driver.find_element_by_xpath("//span[contains(text(), '{}')]".format(visibility)).click()
            elif visibility == "Public":
                context.driver.find_element_by_xpath("//span[contains(text(), '{}')]".format(visibility)).click()
                context.driver.find_element(*self.yes_make_board_public_btn).click()
        context.driver.find_element(*self.create_board_btn).click()
        return "test-board-{}".format(time_stamp)

    def get_board_name(self, context):
        """
        Function to get board name/title
        :param context: driver: Browser Instance
        :return: string: return name of the board
        """
        Base.wait_for_element_staleness(context, context.driver.find_element(*self.board_name_title_lbl), 10)
        return context.driver.find_element(*self.board_name_title_lbl).text
