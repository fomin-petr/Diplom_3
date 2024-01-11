from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    @allure.step('Проверка загрузки страницы Личного кабинета')
    def check_profile_page_loaded(self):
        return self.check_element_present(ProfilePageLocators.PROFILE_BUTTON)

    @allure.step('Ожидание закгрузки страницы Личного кабинета')
    def wait_for_profile_page_loaded(self):
        return self.wait_for_element_located(ProfilePageLocators.PROFILE_BUTTON[1])

    @allure.step('Клик по кнопке История заказов')
    def click_orders_history_button(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Ожидание загрузки Истории заказов')
    def wait_for_orders_history_loaded(self):
        return self.wait_for_element_located(ProfilePageLocators.ORDER_LIST_ITEM[1])

    @allure.step('Ждать пока закончится анимация загрузки Modal_overlay')
    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(ProfilePageLocators.MODAL_OVERLAY)

    @allure.step('Клик по кнопке Выход')
    def click_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Получить номер заказа пользователя из истории заказов')
    def get_user_order_id_from_history(self):
        return self.return_text_in_element(ProfilePageLocators.ORDER_ID)

    @allure.step('Клик по кнопке Лента заказов')
    def click_on_feed_button(self):
        self.click_on_element(MainPageLocators.FEED_BUTTON)
