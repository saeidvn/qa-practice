from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import USER_CREDENTIALS

def test_add_product_to_cart(driver):
    valid_user = next(user for user in USER_CREDENTIALS if user[2] == "success")
    username, password, _ = valid_user

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_item_count() == "1", "Cart count is incorrect!"