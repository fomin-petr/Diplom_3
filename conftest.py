import allure
import pytest
from selenium import webdriver
from data import Urls
import helper
from pages.login_page import LoginPage
from pages.main_page import MainPage
from os import getenv
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', choices=("chrome", "firefox"))


@allure.step('Получение тестируемого браузера из командной строки')
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("browser")


@allure.step('Открытие выбранного браузера на главной странице сайта')
@pytest.fixture
def main_page(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.main_page)
    yield driver
    driver.quit()


@allure.step('Открытие выбранного браузера на странице авторизации')
@pytest.fixture
def login_page(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.login_page)
    yield driver
    driver.quit()


@allure.step('Открытие выбранного браузера на странице восстановления пароля')
@pytest.fixture
def forgot_password_page(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.forgot_password_page)
    yield driver
    driver.quit()


@allure.step('Открытие выбранного браузера на главной странице сайта с предварительной авторизацией юзера')
@pytest.fixture
def main_page_logged_in(browser):
    access_token, email, user, password = helper.create_user()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.login_page)
    page = LoginPage(driver)
    page.wait_for_overlay_disappear()
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    page = MainPage(driver)
    page.wait_for_main_page_loaded()
    yield driver
    driver.quit()
    helper.delete_user(access_token)


@allure.step('Открытие выбранного браузера на главной странице сайта с предварительной авторизацией юзера и созданным заказом')
@pytest.fixture
def main_page_logged_in_with_created_order(browser):
    access_token, email, user, password = helper.create_user()
    helper.create_order_for_authorized_user(access_token)
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.login_page)
    page = LoginPage(driver)
    page.wait_for_overlay_disappear()
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    page = MainPage(driver)
    page.wait_for_main_page_loaded()
    yield driver
    driver.quit()
    helper.delete_user(access_token)


@allure.step('Открытие выбранного браузера на странице Лента заказов')
@pytest.fixture
def feed_page(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.get(Urls.feed_page)
    yield driver
    driver.quit()
