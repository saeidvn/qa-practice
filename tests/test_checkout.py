from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from utils.test_data import USER_CREDENTIALS, get_random_checkout_data
from config import config


def test_complete_checkout_process(driver):
    valid_user = next(user for user in USER_CREDENTIALS if user[2] == "success")
    username, password, _ = valid_user

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    driver.get(f"{config.BASE_URL}cart.html")
    driver.find_element("id", "checkout").click()

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
    assert success_msg == "Thank you for your order!", f"Expected success message, but got: {success_msg}"