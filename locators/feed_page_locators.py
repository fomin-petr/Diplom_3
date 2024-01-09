from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_HEADER = '//h1[ text()="Лента заказов" ]'
    FIRST_ORDER_FROM_LIST = [By.XPATH, '//ul[ contains(@class, "OrderFeed_list") ]/li[1]']
    ORDER_DETAILS_MODAL_WINDOW = [By.XPATH, '//p[ text()[contains(., "#0")] ]/parent::div/parent::div[ contains(@class, "Modal_modal__container") ]']
    ORDER_IN_LIST_BY_ID = [By.XPATH, '//p[ text()[contains(., "{}")] ]']
    TOTAL_ORDERS_COUNTER = [By.XPATH, '//p[ text()[contains (., "Выполнено за все время:")] ]/parent::div/p[ contains(@class, "digits") ]']
    TODAY_ORDERS_COUNTER = [By.XPATH, '//p[ text()[contains (., "Выполнено за сегодня:")] ]/parent::div/p[ contains(@class, "digits") ]']
    LOGO_BUTTON = [By.XPATH, '//div[ contains(@class, "header__logo") ]/a']
    ORDERS_IN_PROGRESS = [By.XPATH, '//ul[ contains(@class, "orderListReady") ]/li']
