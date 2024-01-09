from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_recover_password(self):
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_LINK)

    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(LoginPageLocators.MODAL_OVERLAY)

    def input_email(self, email):
        self.input_in_field(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    def input_password(self, password):
        self.input_in_field(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    def wait_for_login_page_loaded(self):
        return self.wait_for_element_located(LoginPageLocators.LOGIN_BUTTON[1])

    def click_constructor_button(self):
        self.click_on_element(LoginPageLocators.CONSTRUCTOR_BUTTON)




