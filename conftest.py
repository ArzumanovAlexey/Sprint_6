import sys
import os
import pytest
from config.config import Config
from selenium import webdriver
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions



@pytest.fixture
def base_page(driver):
    """Фикстура для базовых методов страниц"""
    return BasePage(driver)

@pytest.fixture
def order_page(driver):
    """Фикстура для методов страницы заказа"""
    return OrderPage(driver)

@pytest.fixture
def main_page(driver):
    """Фикстура для методов главной страницы"""
    return MainPage(driver)
    
@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации WebDriver"""
    browser_name = getattr(Config, "BROWSER", "firefox").lower()

    if browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("-private")  # приватное окно
        driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    else:
        raise RuntimeError(f"Неизвестный браузер в Config.BROWSER: {browser_name}")

    driver.maximize_window()
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()