import allure

from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Ожидание загрузки страницы Лента заказов')
    def wait_for_feed_page_loaded(self):
        return self.wait_for_element_located(FeedPageLocators.FEED_HEADER)

    @allure.step('Клик по верхнему заказу из списка заказов')
    def click_on_top_order_from_list(self):
        self.click_on_element(FeedPageLocators.FIRST_ORDER_FROM_LIST)

    @allure.step('Ожидание появление модального окна с деталями заказа')
    def wait_for_order_details_modal_window(self):
        return self.wait_for_element_located(FeedPageLocators.ORDER_DETAILS_MODAL_WINDOW[1])

    @allure.step('Поиск заказа в ленте по номеру, если найден, возврат True')
    def find_order_in_feed_by_id(self, order_id):
        return self.wait_for_element_located(FeedPageLocators.ORDER_IN_LIST_BY_ID[1].format(order_id))

    @allure.step('Получение числа заказов за всё время')
    def get_total_orders_counter_value(self):
        return self.return_text_in_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)

    @allure.step('Получение числа заказов за сенгодня')
    def get_today_orders_counter_value(self):
        return self.return_text_in_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Клик на логотипе сайта в хэдере')
    def click_on_label_button(self):
        self.click_on_element(FeedPageLocators.LOGO_BUTTON)

    @allure.step('Ожидание появление заказа в Работе по номеру заказа')
    def check_order_is_displayed_in_progress(self, order_id):
        return self.wait_for_text_in_element(FeedPageLocators.ORDERS_IN_PROGRESS[1], order_id)
