from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
import allure


class TestFeed:
    @allure.title('Проверка открытия модального окна с деталями заказа')
    @allure.description('Клик на верхнем заказе в Ленте заказов открывает окно с деталями заказа')
    def test_click_on_order_opens_modal_details_window(self, feed_page):
        self.driver = feed_page
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        page.click_on_top_order_from_list()
        assert page.wait_for_order_details_modal_window()

    @allure.title('Проверка отображения заказов из истории заказов пользователя в Ленте заказов')
    @allure.description('Создать заказ зарегистрированным пользователем и найти этот заказ по номеру в Ленте заказов')
    def test_orders_from_user_profile_history_displayed_in_feed(self, main_page_logged_in_with_created_order):
        self.driver = main_page_logged_in_with_created_order
        page = MainPage(self.driver)
        page.wait_for_overlay_disappear()
        page.click_profile_button()
        page = ProfilePage(self.driver)
        page.wait_for_profile_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_orders_history_button()
        page.wait_for_orders_history_loaded()
        order_id_in_history = page.get_user_order_id_from_history()
        page.click_on_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        assert page.find_order_in_feed_by_id(order_id_in_history)

    @allure.title('Проверка увеличения числа заказов за всё время при создании заказа')
    @allure.description('Взять число заказов за всё время из Ленты заказов, создать новый заказ и проверить новое число заказов за всё время')
    def test_total_orders_counters_increase_after_creating_order(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        total_counter_0 = page.get_total_orders_counter_value()
        page.click_on_label_button()
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        page.wait_for_order_confirmation_modal_window()
        page.wait_for_overlay_disappear()
        page.close_order_details_window_by_clicking_x()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        total_counter_1 = page.get_total_orders_counter_value()
        assert total_counter_1 > total_counter_0

    @allure.title('Проверка увеличения числа заказов за сегодня при создании заказа')
    @allure.description('Взять число заказов за всё время из Ленты заказов, создать новый заказ и проверить новое число заказов за сегодня')
    def test_today_orders_counters_increase_after_creating_order(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.wait_for_overlay_disappear()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        today_counter_0 = page.get_today_orders_counter_value()
        page.click_on_label_button()
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        page.wait_for_order_confirmation_modal_window()
        page.wait_for_overlay_disappear()
        page.close_order_details_window_by_clicking_x()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        today_counter_1 = page.get_today_orders_counter_value()
        assert today_counter_1 > today_counter_0

    @allure.title('Проверка отображения заказа в Ленте заказов в разделе В работе')
    @allure.description('Создать заказ на главной странице и проверить его появление в разделе В работе в Ленте заказов')
    def test_created_order_id_displayed_in_progress(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.wait_for_main_page_loaded()
        page.wait_for_overlay_disappear()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        page.wait_for_order_confirmation_modal_window()
        page.wait_for_animation_gone_when_creating_order()
        order_id = page.get_new_order_id()
        page.close_order_details_window_by_clicking_x()
        page.wait_for_overlay_disappear()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.wait_for_feed_page_loaded()
        assert page.check_order_is_displayed_in_progress(order_id)
