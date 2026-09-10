from selenium.webdriver.common.by import By

from core.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    FIRST_ADD_BUTTON = (
        By.XPATH,
        "(//button[starts-with(@id, 'add-to-cart')])[1]"
    )
    CART_ITEM_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

    def is_loaded(self):
        return self.is_displayed(self.TITLE)

    def add_first_item_to_cart(self):
        self.click(self.FIRST_ADD_BUTTON)

    def get_cart_item_count(self):
        return self.get_text(self.CART_ITEM_COUNT)
