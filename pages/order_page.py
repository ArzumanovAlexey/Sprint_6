from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from datetime import date
from locators.order_page_locators import OrderPageLocators
import random as r


class OrderPage(BasePage):
    """Методы для работы со страницей заказа"""
    
    @staticmethod
    def user_data():
        """Генерация случайных тестовых данных пользователя"""
        
        names = ['Иван', 'Петр', 'Коля', 'Ваня', 'Сергей']
        surnames = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Смирнов']
        metro_stations = ['Бульвар Рокоссовского', 'Спартак', 'Красные ворота', 'Лихоборы']
        rental_period = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']
        color = ['серая безысходность', 'чёрный жемчуг']
        user_data = {
                    'name': r.choice(names), 
                    'surname': r.choice(surnames),
                    'address': 'Москва, улица Большая Лубянка, 20с2',
                    'metro': r.choice(metro_stations),
                    'phone': f'+7{r.randint(1111111111, 9999999999)}',
                    'date': f'{date.today()}',
                    'period': r.choice(rental_period),
                    'color': r.choice(color),
                    'comment': 'Позвонить по телефону за 15 минут' 
                }
        return user_data
    
    @staticmethod
    def get_order_test_data():
        """Возвращает тестовые случаи для заказов"""
        
        return [
            (MainPageLocators.ORDER_BTN_HEADER, OrderPage.user_data()),
            (MainPageLocators.ORDER_BTN_FOOTER, OrderPage.user_data())
        ]
    
    def select_metro_station_from_dropdown(self, test_data):
        """Выбор станции метро из выпадающего списка"""

        self.find_element(OrderPageLocators.METRO_STATION_INPUT).send_keys(test_data['metro'])
        self.find_element(OrderPageLocators.METRO_STATION_OPTION).click()
        
    def select_scooter_color(self, color):
        """Выбирает цвет самоката"""
        
        match color.lower():
            case 'чёрный жемчуг':
                checkbox = self.find_element(OrderPageLocators.COLOR_BLACK_CHECKBOX)
                checkbox.click()
            case 'серая безысходность':
                checkbox = self.find_element(OrderPageLocators.COLOR_GREY_CHECKBOX)
                checkbox.click()
            case _:
                raise ValueError(f"Неизвестный цвет: {color}")
        
    def select_rental_period(self, test_data):
        """Выбор периода аренды из выпадающего списка"""       
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        for option in options:
            if option.text.strip() == test_data['period']:
                option.click()
                return True
        
        raise ValueError(f"Опция '{test_data['period']}' не найдена в дропдауне")
        
    def populate_user_form_by_user_data(self, test_data):
        """Заполнение первой формы заказа (личные данные)"""
        
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(test_data['name'])
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(test_data['surname'])
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(test_data['address'])
        self.select_metro_station_from_dropdown(test_data)
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(test_data['phone'])
        
    def populate_order_form_by_user_data(self, test_data):
        """Заполнение второй формы заказа (данные аренды)"""
        
        self.find_element(OrderPageLocators.DATE_INPUT).send_keys(test_data['date'])
        self.select_rental_period(test_data)
        self.select_scooter_color(test_data['color'])
        self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(test_data['comment'])
    
    def click_next_button(self):
        """Клик по кнопке перехода к следующей форме"""
        
        self.click(OrderPageLocators.NEXT_BUTTON)
        
    def click_order_button(self):
        """Клик по кнопке оформления заказа"""
        
        self.click(OrderPageLocators.ORDER_BUTTON)    
            
    def confirm_order(self):
        """Подтверждение заказа в модальном окне"""

        yes_button = self.find_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        yes_button.click()
    
    def check_success_message_displayed(self):
        """Проверка отображения сообщения об успешном заказе"""
        
        success_message = self.find_element(OrderPageLocators.SUCCESS_MESSAGE)
        return success_message.text
        