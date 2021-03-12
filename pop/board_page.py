from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from features.common.base import Base


class BoardPage:
    list_headers = (By.XPATH, "//div[@class='list-header js-list-header u-clearfix is-menu-shown']//textarea")
    add_another_list_btn = (By.XPATH, "//span[text()='Add another list']")
    new_list_name_txt = (By.CSS_SELECTOR, "input[name='name']")
    add_new_list_btn = (By.CSS_SELECTOR, "input[value='Add List']")
    add_card_btn = (By.CSS_SELECTOR, "input[value='Add Card']")
    add_card_close_btn = (By.CSS_SELECTOR, ".icon-lg.icon-close.dark-hover.js-cancel-edit")
    add_members_btn = (By.XPATH, "//span[text()='Members']")
    current_logged_in_members_btn = (By.CSS_SELECTOR, ".name.js-select-member")
    members_popup_close_btn = (By.CSS_SELECTOR, ".pop-over-header-close-btn.icon-sm.icon-close")
    comment_txt = (By.CSS_SELECTOR, ".comment-box-input.js-new-comment-input")
    comment_save_btn = (By.CSS_SELECTOR, "input[value=Save]")
    assigned_member_icon = (By.CSS_SELECTOR, ".list-card-members.js-list-card-members .member.js-member-on-card-menu")
    added_comment_lbl = (By.CSS_SELECTOR,
                         ".js-list-actions.mod-card-back .current-comment.js-friendly-links.js-open-card p")
    updated_list_headers = (By.XPATH, "//div[@class='list js-list-content']//h2")
    card_popup_close_btn = (By.CSS_SELECTOR, "a[class='icon-md icon-close dialog-close-button js-close-window']")
    list_add_card_close_btb = (By.CSS_SELECTOR, "a[class='icon-lg icon-close dark-hover js-cancel']")

    def add_list_to_board(self, context, list_name):
        """
        Function to add list to board
        :param context: driver: Browser Instance
        :param list_name: contain list names as string
        """
        list_names = list_name.split(",")
        loc_list = context.driver.find_elements(*self.list_headers)
        for index in range(len(list_names)):
            if len(loc_list) == 0 or index > 2:
                if not context.driver.find_element(*self.new_list_name_txt).is_displayed():
                    context.driver.find_element(*self.add_another_list_btn).click()
                context.driver.find_element(*self.new_list_name_txt).clear()
                context.driver.find_element(*self.new_list_name_txt).send_keys(list_names[index])
                context.driver.find_element(*self.add_new_list_btn).click()
            else:
                loc_list[index].clear()
                loc_list[index].send_keys(list_names[index])
        context.driver.find_element(*self.add_card_close_btn).click()

    def add_card_to_list(self, context, card_name, list_name):
        """
        Function to add cards to list
        :param context: driver: Browser Instance
        :param card_name: Card name to Add in list
        :param list_name: on which list name need to add card
        """
        add_card_btn_ele = context.driver. \
            find_element_by_xpath(
                "//h2[text()='{}']//ancestor::div[@class='list js-list-content']"
                "//span[text()='Add a card']".format(
                    list_name))
        if add_card_btn_ele.is_displayed():
            add_card_btn_ele.click()
        card_names = card_name.split(",")
        for card_name in card_names:
            context.driver. \
                find_element_by_xpath(
                    "//h2[text()='{}']//ancestor::div[@class='list js-list-content']"
                    "//div[@class='list-card-details u-clearfix']//textarea"
                    .format(list_name)).send_keys(card_name)
            context.driver.find_element(*self.add_card_btn).click()
        context.driver.find_element(*self.list_add_card_close_btb).click()

    def move_card_to_list(self, context, card_name, from_list, to_list):
        """
        Function to move Card from one list to another list
        :param context: driver: Browser Instance
        :param card_name: name of the card want to move
        :param from_list: from which list need to move
        :param to_list: to which list need to move
        """
        source_card = context \
            .driver \
            .find_element_by_xpath("//div[contains(@class,'js-list-header')]//h2[text()='{from_list}']//..//"
                                   "..//span[@class='list-card-title js-card-name' and contains(text(),'{card}')]"
                                   .format(from_list=from_list, card=card_name))
        destination_card = context.driver \
            .find_element_by_xpath("//h2[@class='list-header-name-assist js-list-name-assist' and text()='{}']/.."
                                   .format(to_list))
        action = ActionChains(context.driver)
        action.drag_and_drop(source_card, destination_card).perform()

    def open_card_from_list(self, context, card_name, from_list):
        """
        Function to open card from specified list
        :param context: driver: Browser Instance
        :param card_name: name of the card to open
        :param from_list: name of the list
        """
        context \
            .driver \
            .find_element_by_xpath("//div[contains(@class,'js-list-header')]//h2[text()='{from_list}']//..//"
                                   "..//span[@class='list-card-title js-card-name' and contains(text(),'{card}')]"
                                   .format(from_list=from_list, card=card_name)).click()

    def assign_member_to_card(self, context, comment):
        """
        Function to assign member to card
        :param context: driver: Browser instance
        :param comment: Message string
        """
        context.driver.find_element(*self.add_members_btn).click()
        context.driver.find_element(*self.current_logged_in_members_btn).click()
        context.driver.find_element(*self.members_popup_close_btn).click()
        context.driver.find_element(*self.comment_txt).send_keys(comment)
        context.driver.find_element(*self.comment_save_btn).click()

    def is_member_icon_added(self, context):
        """
        Function to check is member icon is displayed after assigned
        :param context: driver: Browser Instance
        :return: boolean
        """
        return context.driver.find_element(*self.assigned_member_icon).is_displayed()

    def get_added_comment(self, context):
        """
        Function to get added comment as text
        :param context: driver: Browser Instance
        :return: string: return inner HTML string
        """
        output = context.driver.find_element(*self.added_comment_lbl).text
        context.driver.find_element(*self.card_popup_close_btn).click()
        return output

    def get_list_name(self, context):
        """
        Function to get list name
        :param context: driver: Browser Instance
        :return: string[]: array of list name
        """
        Base.wait_for_element_present(context, self.updated_list_headers, 10)
        loc_list = context.driver.find_elements(*self.updated_list_headers)

        list_title = []
        for loc in loc_list:
            list_title.append(context.driver.execute_script("return arguments[0].innerText", loc))
        return list_title

