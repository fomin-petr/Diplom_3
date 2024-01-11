from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCT_BURGER_HEADER = [By.XPATH, '//h1[ text()="Соберите бургер" ]']
    LOGO_BUTTON = [By.XPATH, '//div[ contains(@class, "header__logo") ]/a']  # кнопка Логотип
    PROFILE_PAGE_BUTTON = [By.XPATH, '//p[ text()="Личный Кабинет" ]']  # кнопка 'Личный кабинет'
    MODAL_OVERLAY = '//div/div[ contains(@class, "Modal_modal_overlay") ]'
    FEED_BUTTON = [By.XPATH, '//*[ text()="Лента Заказов" ]']
    BURGER_CONSTRUCTOR = [By.XPATH, '//ul[ contains(@class, "BurgerConstructor") ]/parent::section']
    CREATE_ORDER_BUTTON = [By.XPATH, '//button[ text()="Оформить заказ" ]']
    ORDER_CONFIRMATION_MODAL_WINDOW = [By.XPATH, '//p[ text()="идентификатор заказа" ]/ancestor::div[ contains(@class, "Modal_modal__container") ]']
    CLOSE_ORDER_CONFIRMATION_MODAL_WINDOW_X_BUTTON = [By.XPATH, '//p[ text()="идентификатор заказа" ]/parent::div/parent::div//button[ contains(@class, "Modal_modal__close") ]']
    LOADING_ANIMATION = [By.XPATH, '//img[ @alt="loading animation" ]/parent::div[ contains(@class, "Modal_modal_opened") ]'] # локатор анимации при создании заказа, означает, что загрузка закончена
    ORDER_ID = [By.XPATH, '//p[ text()="идентификатор заказа" ]/parent::div/h2']


class IngredientsLocators:
    BUN_1 = [By.XPATH, '//*[ text()="Флюоресцентная булка R2-D3" ]/parent::a']
    INGREDIENT_DETAILS_MODAL_WINDOW = [By.XPATH, '//h2[ text()="Детали ингредиента" ]']
    CLOSE_INGREDIENT_DETAILS_MODAL_WINDOW_X_BUTTON = [By.XPATH, '//h2[ text()="Детали ингредиента" ]/parent::div/parent::div//button[ contains(@class, "Modal_modal__close") ]']
    BUN_1_COUNTER = [By.XPATH, '//*[ text()="Флюоресцентная булка R2-D3" ]/parent::a//p[ contains(@class, "counter") ]']
