from locators.main_page_locators import MainPageLocators, IngredientsLocators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_main_page_loaded(self):
        return self.wait_for_element_located(MainPageLocators.CONSTRUCT_BURGER_HEADER[1])

    @allure.step('Проврека что главная страница загружена')
    def check_main_page_laoded(self):
        return self.check_element_present(MainPageLocators.LOGO_BUTTON)

    @allure.step('Ждать пока закончится анимация загрузки Modal_overlay')
    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_profile_button(self):
        self.click_on_element(MainPageLocators.PROFILE_PAGE_BUTTON)

    @allure.step('Клик по кнопке Лента заказов')
    def click_feed_button(self):
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step('Клик на ингредиенте булочка_1')
    def click_on_ingredient(self):
        self.click_on_element(IngredientsLocators.BUN_1)

    @allure.step('Ожидание загрузки модального окна с деталями ингредиента')
    def wait_for_ingredient_modal_window(self):
        return self.wait_for_element_located(IngredientsLocators.INGREDIENT_DETAILS_MODAL_WINDOW[1])

    @allure.step('Закрыть модальное окно с деталями ингредиента')
    def close_ingredient_details_window_by_clicking_x(self):
        self.click_on_element(IngredientsLocators.CLOSE_INGREDIENT_DETAILS_MODAL_WINDOW_X_BUTTON)

    @allure.step('Ожидание закрытия модального окна с деталями ингредиента')
    def wait_for_ingredient_modal_window_closed(self):
        return self.wait_for_invisibility_of_element_located(IngredientsLocators.INGREDIENT_DETAILS_MODAL_WINDOW[1])

    @allure.step('Добавить ингредиент булочка_1 в заказ драг-энд-дропом')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(IngredientsLocators.BUN_1, MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step('Получить счетчик количества ингредиента в заказе булочка_1')
    def check_counter_of_bun_added_to_constructor(self):
        return self.return_text_in_element(IngredientsLocators.BUN_1_COUNTER)

    @allure.step('Клик на конпке Создать заказ')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание появления модального окна с деталями заказа')
    def wait_for_order_confirmation_modal_window(self):
        return self.wait_for_element_located(MainPageLocators.ORDER_CONFIRMATION_MODAL_WINDOW[1])

    @allure.step('Закрытие модального окна с деталями заказа кликом по Х')
    def close_order_details_window_by_clicking_x(self):
        self.click_on_element(MainPageLocators.CLOSE_ORDER_CONFIRMATION_MODAL_WINDOW_X_BUTTON)

    @allure.step('Ожидание окончания анимации в модальном окне с деталями заказа')
    def wait_for_animation_gone_when_creating_order(self):
        return self.wait_for_invisibility_of_element_located(MainPageLocators.LOADING_ANIMATION[1])

    @allure.step('Получение номера созданного заказа')
    def get_new_order_id(self):
        return self.return_text_in_element(MainPageLocators.ORDER_ID)
