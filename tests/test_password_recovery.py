from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
import helper
import allure


class TestPasswordRecovery:
    @allure.title('Проверка клика по ссылке Восстановить пароль переводит на соответствующую страницу')
    @allure.description('Со страницы авторизации кликнуть по ссылке Восстановить пароль - откроет страница восстановления пароля')
    def test_click_on_password_recovery_link(self, login_page):
        self.driver = login_page
        page = LoginPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_recover_password()
        page = ForgotPasswordPage(self.driver)
        assert page.check_password_recover_page_loaded()

    @allure.title('Проверка перехода на страницу сброса пароля после ввода email')
    @allure.description('Ввести email зарегистрированного юзера на странице восстановления пароля')
    def test_input_email_and_click_recover_button(self, forgot_password_page):
        access_token, email, user, password = helper.create_user()
        self.driver = forgot_password_page
        page = ForgotPasswordPage(self.driver)
        page.click_email_input_field()
        page.input_email(email)
        page.click_recover_button()
        page = ResetPasswordPage(self.driver)
        page.wait_for_reset_password_page_loaded()
        page.wait_for_overlay_disappear()
        assert page.check_reset_page_laoded()
        helper.delete_user(access_token)

    @allure.title('Проверка клика на иконку Показать пароль делает поле активным и появляется граница поля')
    @allure.description('Перейти на страницу сброса пароля зарегистрированным юзером и нажать на иконку Показать пароль '
                        '- граница поля изменится и окно странет активным')
    def test_click_on_show_hide_password_activates_field(self, forgot_password_page):
        access_token, email, user, password = helper.create_user()
        self.driver = forgot_password_page
        page = ForgotPasswordPage(self.driver)
        page.click_email_input_field()
        page.input_email(email)
        page.click_recover_button()
        page = ResetPasswordPage(self.driver)
        page.check_reset_page_laoded()
        page.wait_for_overlay_disappear()
        page.click_show_password_button()
        assert page.check_password_input_field_active()
        helper.delete_user(access_token)
