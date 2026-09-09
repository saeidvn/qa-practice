import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USER_CREDENTIALS

@pytest.mark.parametrize("username, password, expected_result",
                         USER_CREDENTIALS,
                         ids=[user[0] for user in USER_CREDENTIALS])
def test_user_login(driver, username, password, expected_result):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if expected_result == "success":
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded(), "User was not redirected to Inventory page!"
    else:
        assert login_page.is_error_message_displayed()