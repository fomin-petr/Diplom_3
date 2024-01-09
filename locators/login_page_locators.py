from selenium.webdriver.common.by import By


class LoginPageLocators:
    RECOVER_PASSWORD_LINK = [By.XPATH, '//a[ @href="/forgot-password" ]'] # кнопка восстановления пароля
    MODAL_OVERLAY = '//div/div[ contains(@class, "Modal_modal_overlay") ]' # перекрывающее сияние при загрузке страницы
    EMAIL_INPUT_FIELD = [By.XPATH, '//input[ contains(@type, "text") ]'] # поле ввода Email
    PASSWORD_INPUT_FIELD = [By.XPATH, '//input[ contains(@type, "password") ]'] # поле ввода пароля
    REGISTRATION_BUTTON = '//a[ text() = "Зарегистрироваться" ]' # Кнопка Зарегистрироваться
    LOGIN_BUTTON = [By.XPATH, '//button[ text() = "Войти" ]'] # Кнопка Зарегистрироваться
    CONSTRUCTOR_BUTTON = [By.XPATH, '//*[ text()="Конструктор" ]']
