import pytest
import allure
from config import BASE_URL

class TestOrder:
    # Тестовые данные
    ORDER_DATA = [
        # Первый набор данных
        {
            "name": "Иван",
            "surname": "Петров",
            "address": "ул. Ленина, д. 10",
            "metro_station": "Сокольники",
            "phone": "89991234567",
            "date": "25.09.2025",
            "rental_period": "сутки",
            "color": "black",
            "comment": "Позвонить за час"
        },
        # Второй набор данных
        {
            "name": "Мария",
            "surname": "Сидорова",
            "address": "пр-т Мира, д. 25",
            "metro_station": "Комсомольская",
            "phone": "89997654321",
            "date": "01.10.2025",
            "rental_period": "трое суток",
            "color": "grey",
            "comment": "Оставить у двери"
        }
    ]
    
    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий заказа через верхнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_through_top_button_success(self, main_page, order_page, order_data):
        with allure.step("Кликнуть на верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()
        
        self._complete_order_flow(order_page, order_data)

    @allure.feature("Заказ самоката")
    @allure.story("Позитивный сценарий заказа через нижнюю кнопку")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_through_bottom_button_success(self, main_page, order_page, order_data):
        with allure.step("Прокрутить к нижней кнопке 'Заказать'"):
            main_page.scroll_to_bottom_order_button()
        
        with allure.step("Кликнуть на нижнюю кнопку 'Заказать'"):
            main_page.click_order_button_bottom()
        
        self._complete_order_flow(order_page, order_data)
    
    def _complete_order_flow(self, order_page, order_data):
        with allure.step("Заполнить информацию о заказчике"):
            order_page.fill_personal_info(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["metro_station"],
                order_data["phone"]
            )
        
        with allure.step("Перейти к следующему шагу"):
            order_page.click_next_button()
        
        with allure.step("Заполнить информацию об аренде"):
            order_page.fill_rental_info(
                order_data["date"],
                order_data["rental_period"],
                order_data["color"],
                order_data["comment"]
            )
        
        with allure.step("Подтвердить заказ"):
            order_page.click_order_button()
            order_page.confirm_order()
        
        with allure.step("Проверить сообщение об успешном заказе"):
            assert order_page.is_success_message_displayed(), "Сообщение об успешном заказе не отображается"
    
    @allure.feature("Навигация")
    @allure.story("Переход на главную страницу через логотип Самоката")
    def test_scooter_logo_navigation(self, main_page):
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
        
        with allure.step("Проверить URL текущей страницы"):
            assert main_page.is_main_page_loaded(), \
                f"Ожидался переход на главную страницу, но текущий URL: {main_page.get_current_url()}"
    
    @allure.feature("Навигация")
    @allure.story("Переход на Дзен через логотип Яндекса")
    def test_yandex_logo_navigation(self, main_page):
        with allure.step("Запомнить текущее окно"):
            main_window = main_page.driver.current_window_handle
        
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
        
        with allure.step("Переключиться на новое окно"):
            main_page.switch_to_new_window()
        
        with allure.step("Проверить, что открылась страница Дзен"):
            assert main_page.is_dzen_page_loaded(), \
                f"Ожидался переход на Дзен, но текущий URL: {main_page.get_current_url()}"
        
        with allure.step("Закрыть новое окно и вернуться к основному"):
            main_page.driver.close()
            main_page.driver.switch_to.window(main_window)