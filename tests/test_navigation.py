import pytest
import allure
from config.config import Config

class TestNavigation:
    """Тесты для проверки навигации по страницам"""
    
    @allure.epic("Самокаты")
    @allure.feature("Навигация")
    @allure.story("Переход на главную страницу")
    @allure.title("Переход на главную страницу через логотип самоката")
    def test_navigation_scooter_logo(self, main_page, base_page):
        """
        Steps:
        1. Перейти на форму оформления заказа
        2. Нажать на логотип самоката
        3. Проверить: выполнился переходна главную страницу
        """ 
        try:
            with allure.step("Перейти на страницу оформления заказа"):
                main_page.click_order_button()
            with allure.step("Проверить переход на страницу заказов"):
                url = base_page.check_page_url('order_page')
                assert url == Config.ORDER_PAGE_URL, \
                    f'Переход на страницу заказа не выполнен, текущий url: {url}'
            with allure.step("Нажать на логотип самоката"):
                main_page.click_scooter_logo()
            with allure.step("Проверить переход на главную страницу"):
                url = base_page.check_page_url('main_page') 
                assert url == Config.BASE_URL, \
                    f'Переход на главную страницу не выполнен, текущий url: {url}'
        
        except Exception as e:
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")
            
    @allure.epic("Самокаты")
    @allure.feature("Навигация")
    @allure.story("Переход на страницу дзена")
    @allure.title("Переход на страницу дзена через логотип Яндекса")
    def test_navigation_yandex_logo(self, main_page, base_page):
        """
        Steps:
        1. Нажать на логотип Яндекса
        2. Проверить: выполнился переходна на страницу дзена
        """ 
        try:
            with allure.step("Нажать на логотип Яндекса"):
                main_page.click_yandex_logo()
            with allure.step("Переключиться на новую вкладку в браузере"):
                base_page.switch_new_window()
            with allure.step("Проверить, что в новой вкладке открылась страница Дзен"):            
                url = base_page.check_page_url(page='dzen_page') 
                assert Config.DZEN_PAGE_URL in url, \
                    f'Переход на страницу дзена не выполнен, текущий url: {url}'
                    
        
        except Exception as e:
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")   