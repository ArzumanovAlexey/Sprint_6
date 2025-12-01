import sys
import os
import pytest
from config.config import Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_configure():
    """Настройка путей перед выполнением тестов"""
    
    # Получаем абсолютный путь к корневой директории проекта
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    # Добавляем корневую директорию в sys.path
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    
    print(f"Project root added to path: {project_root}")

@pytest.fixture
def base_page(driver):
    """Фикстура для базовых методов страниц"""
    from pages.base_page import BasePage
    return BasePage(driver)

@pytest.fixture
def order_page(driver):
    """Фикстура для методов страницы заказа"""
    from pages.order_page import OrderPage
    return OrderPage(driver)

@pytest.fixture
def main_page(driver):
    """Фикстура для методов главной страницы"""
    from pages.main_page import MainPage
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