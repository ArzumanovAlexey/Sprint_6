from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class MainPage(BasePage):
    # Локаторы для вопросов
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    ANSWER_LOCATORS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
    
    # Локаторы для кнопок заказа
    ORDER_BUTTON_TOP =    (By.XPATH, "//button[contains(text(), 'Заказать') and parent::div[@class='Header_Nav__AGCXC']]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать') and parent::div[@class='Home_FinishButton__1_cWm']]")
    
    # Локаторы логотипов
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.base_url)
    
    def click_question(self, question_index):
        #Клик на вопрос по индексу
        locator = self.QUESTION_LOCATORS[question_index]
        self.click_element(locator)
    
    def get_answer_text(self, answer_index):
        #Получить текст ответа по индексу
        locator = self.ANSWER_LOCATORS[answer_index]
        return self.find_element(locator).text
    
    def is_answer_displayed(self, answer_index):
        #Проверить, отображается ли ответ
        locator = self.ANSWER_LOCATORS[answer_index]
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def click_order_button_top(self):
        #Клик на верхнюю кнопку заказа
        self.click_element(self.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        #Клик на нижнюю кнопку заказа
        self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        #Клик на логотип Самоката
        self.click_element(self.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        #Клик на логотип Яндекса
        self.click_element(self.YANDEX_LOGO)
    
    def scroll_to_questions(self):
        #Прокрутить к разделу с вопросами
        questions_section = self.find_element((By.ID, "accordion__heading-0"))
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_section)
        
    def scroll_to_bottom_order_button(self):
        #Прокрутить к нижней кнопке заказа
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
    
    def is_main_page_loaded(self):
        #Проверить, что загружена главная страница
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: self.base_url in driver.current_url
            )
            return True
        except:
            return False
    
    def is_dzen_page_loaded(self):
        #Проверить, что загружена страница Дзен
        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: "dzen.ru" in driver.current_url
            )
            return True
        except:
            return False