from selenium.webdriver.common.by import By

from config import config
from core.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open(self):
        self.driver.get(f"{config.BASE_URL}cart.html")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
