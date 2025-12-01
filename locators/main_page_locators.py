from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""

    # Блок с вопросами и ответами (FAQ)
    QUESTIONS_TEXT = (By.CSS_SELECTOR, "div.accordion__button")
    QUESTION_ITEMS = (By.CSS_SELECTOR, "div.accordion__item")
    ANSWERS = (By.CSS_SELECTOR, "div.accordion__panel")
    ANSWERS_TEXT = (By.CSS_SELECTOR, "div.accordion__panel p")
    
    # Локаторы конкретных вопросов
    PRICE_QUESTION = (By.ID, "accordion__heading-0")
    ORDER_SEVERAL_SCOOTERS_QUESTION = (By.ID, "accordion__heading-1")
    ORDER_TIME_QUESTION = (By.ID, "accordion__heading-2")
    TODAY_ORDER_QUESTION = (By.ID, "accordion__heading-3")
    EXTEND_ORDER_QUESTION = (By.ID, "accordion__heading-4")
    CHARGER_QUESTION = (By.ID, "accordion__heading-5")
    CANCEL_ORDER_QUESTION = (By.ID, "accordion__heading-6")
    OUTSIDE_MKAD_ORDER_QUESTION = (By.ID, "accordion__heading-7")
    
    # Локаторы конкретных ответов
    PRICE_ANSWER = (By.ID, "accordion__panel-0")
    ORDER_SEVERAL_SCOOTERS_ANSWER = (By.ID, "accordion__panel-1")
    ORDER_TIME_ANSWER = (By.ID, "accordion__panel-2")
    TODAY_ORDER_ANSWER = (By.ID, "accordion__panel-3")
    EXTEND_ORDER_ANSWER = (By.ID, "accordion__panel-4")
    CHARGER_ANSWER = (By.ID, "accordion__panel-5")
    CANCEL_ORDER_ANSWER = (By.ID, "accordion__panel-6")
    OUTSIDE_MKAD_ORDER_ANSWER = (By.ID, "accordion__panel-7")

    # Кнопки заказа
    ORDER_BTN_HEADER = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")
    ORDER_BTN_FOOTER = (By.XPATH, "//div[contains(@class, 'Home')]//button[text()='Заказать']")
    
    # Логотипы
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")