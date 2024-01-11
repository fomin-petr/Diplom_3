from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
import allure


class TestMainFunctionality:
    @allure.title('Проверка клика на кнопке Конструктор')
    @allure.description('Клик на кнопке конструктор переходит на главную страницу сайта')
    def test_click_constructor_button(self, login_page):
        self.driver = login_page
        page = LoginPage(self.driver)
        page.wait_for_login_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_constructor_button()
        page = MainPage(self.driver)
        assert page.wait_for_main_page_loaded()

    @allure.title('Проверка клика на кнопке Лента заказов')
    @allure.description('Клик на кнопке Лента заказов переходит на соответствующуюю страницу')
    def test_click_feed_button(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.click_feed_button()
        page = FeedPage(self.driver)
        assert page.wait_for_feed_page_loaded()

    @allure.title('Проверка клика на ингредиенте')
    @allure.description('Клик на ингредиенте открывает окно с деталями ингредиента')
    def test_click_on_ingredient(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.click_on_ingredient()
        assert page.wait_for_ingredient_modal_window()

    @allure.title('Проверка закрытия модального окна с деталями ингредиента')
    @allure.description('Открыть модальное окно с деталями ингредиента и закрыть кликнув на Х')
    def test_close_ingredient_details_modal_window_by_clicking_x(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.click_on_ingredient()
        page.wait_for_ingredient_modal_window()
        page.close_ingredient_details_window_by_clicking_x()
        assert page.wait_for_ingredient_modal_window_closed()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении его в конструктор заказа')
    @allure.description('Перетащить драг и дропом ингредиент в конструктор заказа и проверить счетчик ингредиента')
    def test_add_ingredient_to_constructor_check_ingredient_counter(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.add_ingredient_to_order()
        assert page.check_counter_of_bun_added_to_constructor() == '2'

    @allure.title('Проверка создания заказа зарегистрированным пользователем')
    @allure.description('При нажатии на кнопку Создать заказ (с добавленными ингредиентами) открывается модальное окно')
    def test_logged_in_user_order_creation(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        assert page.wait_for_order_confirmation_modal_window()
