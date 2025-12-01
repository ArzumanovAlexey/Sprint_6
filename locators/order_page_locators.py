from selenium.webdriver.common.by import By

class OrderPageLocators:
    """Локаторы для страницы заказа"""
    
    # Форма "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    
    # Форма "Про аренду"
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-arrow")
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопки оформления заказа
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")    
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    CANCEL_ORDER_BUTTON = (By.XPATH, "//button[text()='Нет']")
    
    # Статус заказа
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    # Подтверждение заказа
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    SUCCESS_MESSAGE_TEXT = (By.CLASS_NAME, "Order_Text__2broi")