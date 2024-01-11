from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    ENTER_CODE_FROM_EMAIL_LABEL = [By.XPATH, "//label[ text()='Введите код из письма' ]"]
    MODAL_OVERLAY = '//div/div[ contains(@class, "Modal_modal_overlay") ]'
    SHOW_PASSWORD_ICON = [By.XPATH, '//div[ contains(@class, "input__icon") ]']
    PASSWORD_INPUT_FIELD = [By.XPATH, "//label[ text()='Пароль' ]/parent::div"]
