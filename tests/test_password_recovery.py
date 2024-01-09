from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
import helper


class TestPasswordRecovery:
    def test_click_on_password_recovery_link(self, login_page):
        self.driver = login_page
        page = LoginPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_recover_password()
        page = ForgotPasswordPage(self.driver)
        assert page.check_password_recover_page_loaded()

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
