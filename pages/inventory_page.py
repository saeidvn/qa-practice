from core.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")

    def is_loaded(self):
        return ("inventory.html" in self.driver.current_url
                and self.is_displayed(self.TITLE))

    def add_first_item_to_cart(self):
        first_add_button = self.driver.find_element("xpath", "(//button[starts-with(@id, 'add-to-cart')])[1]")
        first_add_button.click()

    def get_cart_item_count(self):
        badge = self.driver.find_element("class name", "shopping_cart_badge")
        return badge.text