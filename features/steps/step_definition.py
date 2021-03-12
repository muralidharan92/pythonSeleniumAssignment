from behave import *

from features.common.base import Base
from pop.add_board_page import AddBoardPage
from pop.board_page import BoardPage
from pop.home_page import HomePage
from pop.login_page import LoginPage


@given('launch "{browser}" browser and open trello')
def launch_browser(context, browser):
    context.driver = Base.open_and_launch_url_in_browser(browser)


@when('user login to the application using username "{username}" and password "{password}"')
def login_to_application(context, username, password):
    login = LoginPage()
    login.perform_login(context, username, password)


@when('click "{board_name}" from board tiles')
def click_create_new_board(context, board_name):
    home = HomePage()
    home.click_board_tile(context, board_name)


@when('add board using with visibility "{visibility}"')
def add_board(context, visibility):
    context.add_board_page = AddBoardPage()
    context.board_name = context.add_board_page.add_board(context, visibility)


@then('verify board added successfully')
def verify_board_created(context):
    board_name = context.add_board_page.get_board_name(context)
    assert board_name == context.board_name


@when('add list with name of "{list_name}"')
def add_list_to_board(context, list_name):
    context.board = BoardPage()
    context.board.add_list_to_board(context, list_name)


@then('verify "{list_name}" list added')
def verify_added_list(context, list_name):
    expected_list = list_name.split(",")
    actual_list = context.board.get_list_name(context)
    assert actual_list == expected_list


@when('create card "{card_name}" under "{list_name}" list')
def create_card_under_list(context, card_name, list_name):
    context.board.add_card_to_list(context, card_name, list_name)


@when('move "{card_name}" from "{from_list}" list to "{to_list}" list')
def move_card_to_lists(context, card_name, from_list, to_list):
    context.board.move_card_to_list(context, card_name, from_list, to_list)


@when('open "{card_name}" card from "{list_name}" list')
def open_card_from_list(context, card_name, list_name):
    context.board.open_card_from_list(context, card_name, list_name)


@when('assign it to current logged in user and add comment as "{comment}"')
def assign_member_and_add_comment(context, comment):
    context.board.assign_member_to_card(context, comment)


@then('verify current user assigned and comment added as "{comment}"')
def verify_member_comment_added(context, comment):
    is_icon_displayed = context.board.is_member_icon_added(context)
    assert is_icon_displayed
    added_comment_text = context.board.get_added_comment(context)
    assert added_comment_text == comment, "Added Comment {} is not matched with {} comment in UI"\
        .format(comment, added_comment_text)
