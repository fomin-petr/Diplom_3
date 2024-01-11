from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    @allure.step('Клик по ссылке Восстановить пароль')
    def click_recover_password(self):
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Ждать пока закончится анимация загрузки Modal_overlay')
    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(LoginPageLocators.MODAL_OVERLAY)

    @allure.step('Ввод email в поле')
    def input_email(self, email):
        self.input_in_field(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Ввод пароля в поле')
    def input_password(self, password):
        self.input_in_field(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Клик на кнопке Войти')
    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_for_login_page_loaded(self):
        return self.wait_for_element_located(LoginPageLocators.LOGIN_BUTTON[1])

    @allure.step('Клик по кнопке Конструктор в хэдере')
    def click_constructor_button(self):
        self.click_on_element(LoginPageLocators.CONSTRUCTOR_BUTTON)
