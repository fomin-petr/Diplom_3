from locators.main_page_locators import MainPageLocators, IngredientsLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def wait_for_main_page_loaded(self):
        return self.wait_for_element_located(MainPageLocators.CONSTRUCT_BURGER_HEADER[1])

    def check_main_page_laoded(self):
        return self.check_element_present(MainPageLocators.LOGO_BUTTON)

    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY)

    def click_profile_button(self):
        self.click_on_element(MainPageLocators.PROFILE_PAGE_BUTTON)

    def click_feed_button(self):
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    def click_on_ingredient(self):
        self.click_on_element(IngredientsLocators.BUN_1)

    def wait_for_ingredient_modal_window(self):
        return self.wait_for_element_located(IngredientsLocators.INGREDIENT_DETAILS_MODAL_WINDOW[1])

    def close_ingredient_details_window_by_clicking_x(self):
        self.click_on_element(IngredientsLocators.CLOSE_INGREDIENT_DETAILS_MODAL_WINDOW_X_BUTTON)

    def wait_for_ingredient_modal_window_closed(self):
        return self.wait_for_invisibility_of_element_located(IngredientsLocators.INGREDIENT_DETAILS_MODAL_WINDOW[1])

    def add_ingredient_to_order(self):
        self.drag_and_drop_element(IngredientsLocators.BUN_1, MainPageLocators.BURGER_CONSTRUCTOR)

    def check_counter_of_bun_added_to_constructor(self):
        return self.return_text_in_element(IngredientsLocators.BUN_1_COUNTER)

    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)

    def wait_for_order_confirmation_modal_window(self):
        return self.wait_for_element_located(MainPageLocators.ORDER_CONFIRMATION_MODAL_WINDOW[1])

    def close_order_details_window_by_clicking_x(self):
        self.click_on_element(MainPageLocators.CLOSE_ORDER_CONFIRMATION_MODAL_WINDOW_X_BUTTON)

    def wait_for_animation_gone_when_creating_order(self):
        return self.wait_for_invisibility_of_element_located(MainPageLocators.LOADING_ANIMATION[1])

    def get_new_order_id(self):
        return self.return_text_in_element(MainPageLocators.ORDER_ID)

