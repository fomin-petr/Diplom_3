from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def check_profile_page_loaded(self):
        return self.check_element_present(ProfilePageLocators.PROFILE_BUTTON)

    def wait_for_profile_page_loaded(self):
        return self.wait_for_element_located(ProfilePageLocators.PROFILE_BUTTON[1])

    def click_orders_history_button(self):
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)

    def wait_for_orders_history_loaded(self):
        return self.wait_for_element_located(ProfilePageLocators.ORDER_LIST_ITEM[1])

    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(ProfilePageLocators.MODAL_OVERLAY)

    def click_logout_button(self):
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    def get_user_order_id_from_history(self):
        return self.return_text_in_element(ProfilePageLocators.ORDER_ID)

    def click_on_feed_button(self):
        self.click_on_element(MainPageLocators.FEED_BUTTON)


