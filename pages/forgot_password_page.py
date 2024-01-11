from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
import allure

class ForgotPasswordPage(BasePage):
    @allure.step('Ожидание загрузки страницы восстановления пароля')
    def check_password_recover_page_loaded(self):
        return self.check_element_present(ForgotPasswordPageLocators.PASSWORD_RECOVER_HEADER)

    @allure.step('Клик по полю ввода email')
    def click_email_input_field(self):
        self.click_on_element(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD)

    @allure.step('Ввод email в поле ввода')
    def input_email(self, email):
        self.input_in_field(ForgotPasswordPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Клик по конпке Восстановить пароль')
    def click_recover_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Ожидание закрытия формы восстановления')
    def check_password_header_gone(self):
        return self.wait_for_invisibility_of_element_located(ForgotPasswordPageLocators.PASSWORD_RECOVER_HEADER[1])
