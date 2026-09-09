from selenium.webdriver.common.by import By
from core.base_page import BasePage
from config import config
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(config.BASE_URL)

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def is_error_message_displayed(self):
        try:
            return self.is_displayed(self.ERROR_MESSAGE)
        except NoSuchElementException:
            return False
