from core.base_page import BasePage
from enums.locators import CheckoutLocators

class CheckoutPage(BasePage):
    def fill_user_info(self, first_name, last_name, postal_code):
        self.type_text(CheckoutLocators.FIRST_NAME_INPUT.value, first_name)
        self.type_text(CheckoutLocators.LAST_NAME_INPUT.value, last_name)
        self.type_text(CheckoutLocators.POSTAL_CODE_INPUT.value, postal_code)

    def click_continue(self):
        self.click(CheckoutLocators.CONTINUE_BUTTON.value)

    def click_finish(self):
        self.click(CheckoutLocators.FINISH_BUTTON.value)

    def get_success_message(self):
        return self.get_text(CheckoutLocators.SUCCESS_MESSAGE.value)