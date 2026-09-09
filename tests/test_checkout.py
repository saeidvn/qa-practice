from config import config
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import USER_CREDENTIALS, get_random_checkout_data


def test_complete_checkout_process(driver):
    valid_user = next(
        user for user in USER_CREDENTIALS
        if user[2] == "success"
    )
    username, password, _ = valid_user

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.open()
    cart_page.click_checkout()

    checkout_data = get_random_checkout_data()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_user_info(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"]
    )
    checkout_page.click_continue()
    checkout_page.click_finish()

    success_msg = checkout_page.get_success_message()

    assert success_msg == "Thank you for your order!", (
        f"Expected success message, but got: {success_msg}"
    )
