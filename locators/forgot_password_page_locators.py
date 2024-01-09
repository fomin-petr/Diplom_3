from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    PASSWORD_RECOVER_HEADER = [By.XPATH, "//h2[ text()='Восстановление пароля' ]"]
    EMAIL_INPUT_FIELD = [By.XPATH, '//div[ contains(@class, "input_type_text") ]/input']
    RECOVER_BUTTON = [By.XPATH, '//button[ text()="Восстановить" ]']
