from selenium.webdriver.common.by import By


class ProfilePageLocators:
    NAME_FIELD = '//label[ text()="Имя"]/parent::div/input' # поле Имя
    LOGIN_FIELD = '//label[ text()="Логин"]/parent::div/input' # поле Логин
    EXIT_BUTTON = '//button[ text()="Выход"]' # кнопка Выйти
    PROFILE_BUTTON = [By.XPATH, "//a[ text()='Профиль' ]"]
    ORDER_HISTORY_BUTTON = [By.XPATH, "//a[ text()='История заказов' ]"]
    ORDER_LIST_ITEM = [By.XPATH, '//li[ contains(@class, "OrderHistory_listItem") ]']
    MODAL_OVERLAY = '//div/div[ contains(@class, "Modal_modal_overlay") ]'
    LOGOUT_BUTTON = [By.XPATH, "//button[ text()='Выход' ]"]
    ORDER_ID = [By.XPATH, '//ul[ contains(@class, "OrderHistory_profileList") ]//div[ contains(@class, "textBox") ]//p[ contains(@class, "type_digits") ]']
