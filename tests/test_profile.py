from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
import allure


class TestProfile:
    @allure.title('Проверка клика по кнопке Личный кабинет на главной странице')
    @allure.description('Клик по кнопке Личный кабинет переводит на страницу кабинета')
    def test_click_profile_button_on_main_page(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_profile_button()
        page = ProfilePage(self.driver)
        page.wait_for_profile_page_loaded()
        assert page.check_profile_page_loaded()

    @allure.title('Проверка клика по кнопке История заказов')
    @allure.description('В личном кабинете зарегестрированного юзера с имеющимися заказами '
                        'кликнуть по кнопке История заказов - откроются его заказы')
    def test_click_orders_history_button(self, main_page_logged_in_with_created_order):
        self.driver = main_page_logged_in_with_created_order
        page = MainPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_profile_button()
        page = ProfilePage(self.driver)
        page.wait_for_profile_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_orders_history_button()
        assert page.wait_for_orders_history_loaded()

    @allure.title('Проверка кнопки Выход в Личном кабинете')
    @allure.description('В личном кабинете зарегистрированного юзера нажать на кнопку Выход - юзер выйдет из системы')
    def test_click_logout_button(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_profile_button()
        page = ProfilePage(self.driver)
        page.wait_for_profile_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_logout_button()
        page = LoginPage(self.driver)
        assert page.wait_for_login_page_loaded()
