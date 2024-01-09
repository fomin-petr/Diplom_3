from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def check_password_recover_page_loaded(self):
        return self.check_element_present(ForgotPasswordPageLocators.PASSWORD_RECOVER_HEADER)

    def click_email_input_field(self):
        self.click_on_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD)

    def input_email(self, email):
        self.input_in_field(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD, email)

    def click_recover_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    def check_password_header_gone(self):
        return self.wait_for_invisibility_of_element_located(ForgotPasswordPageLocators.PASSWORD_RECOVER_HEADER[1])
