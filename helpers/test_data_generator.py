from datetime import date
import random as r
from locators.main_page_locators import MainPageLocators


def generate_user_data():
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


def get_order_test_data():
    """Возвращает тестовые случаи для заказов"""
    
    return [
        (MainPageLocators.ORDER_BTN_HEADER, generate_user_data()),
        (MainPageLocators.ORDER_BTN_FOOTER, generate_user_data())
    ]


def get_qa_data():
    """Получить тестовые данные для проверки вопросов и ответов"""
    
    return [
        (MainPageLocators.PRICE_QUESTION, MainPageLocators.PRICE_ANSWER, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (MainPageLocators.ORDER_SEVERAL_SCOOTERS_QUESTION, MainPageLocators.ORDER_SEVERAL_SCOOTERS_ANSWER, "один заказ — один самокат"),
        (MainPageLocators.ORDER_TIME_QUESTION, MainPageLocators.ORDER_TIME_ANSWER, " когда вы оплатите заказ"),
        (MainPageLocators.TODAY_ORDER_QUESTION, MainPageLocators.TODAY_ORDER_ANSWER, "с завтрашнего дня"),
        (MainPageLocators.EXTEND_ORDER_QUESTION, MainPageLocators.EXTEND_ORDER_ANSWER, "номеру 1010"),
        (MainPageLocators.CHARGER_QUESTION, MainPageLocators.CHARGER_ANSWER, "полной зарядкой"),
        (MainPageLocators.CANCEL_ORDER_QUESTION, MainPageLocators.CANCEL_ORDER_ANSWER, "Штрафа не будет"),
        (MainPageLocators.OUTSIDE_MKAD_ORDER_QUESTION, MainPageLocators.OUTSIDE_MKAD_ORDER_ANSWER, "Всем самокатов!"),
    ]

