from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    """Методы для работы с главной страницей"""
    
    def click_question(self, question_locator):
        """Кликнуть на вопрос в секции FAQ"""
        
        question_element = self.find_element(question_locator)
        if question_element is None:
            raise AssertionError(f"Элемент вопроса не найден: {question_locator}")
        self.scroll_to_element_center(question_element)
        self.click_element_via_script(question_element)
        return question_element
    
    def click_order_button(self, btn_locator=None):
        """Кликнуть на кнопку заказа в хедере или футере"""
        order_button = btn_locator or MainPageLocators.ORDER_BTN_HEADER
        self.scroll_to_element(order_button)
        self.click(order_button)
    
    def click_scooter_logo(self):
        """Клик на логотип Самоката"""    
        self.click(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        """Клик на логотип Яндекса"""
        self.click(MainPageLocators.YANDEX_LOGO)
            
    def get_answer_text(self, answer_locator):
        """Получить текст ответа"""
        
        answer_element = self.find_element(answer_locator)
        if answer_element is None:
            raise AssertionError(f"Элемент ответа не найден: {answer_locator}")
        return answer_element.text.strip()
              
    def qa_dictionary(self, items_locator=None, question_locator=None, answer_locator=None):
        """Создает словарь вопрос-ответ для всех FAQ элементов"""
        
        items_locator = items_locator or MainPageLocators.QUESTION_ITEMS
        question_locator = question_locator or MainPageLocators.QUESTIONS_TEXT
        answer_locator = answer_locator or MainPageLocators.ANSWERS_TEXT
        
        self.scroll_to_element(question_locator)       
        items = self.find_elements(items_locator)
        faq_dict = {}
        
        for item in items:
            try:
                # Извлекаем вопрос
                question_element = item.find_element(*question_locator)
                question = question_element.text.strip()
                
                question_element.click()
                
                # Извлекаем ответ
                answer_element = item.find_element(*answer_locator)
                answer = answer_element.text.strip()
                self.scroll_to_bottom()

                if question and answer:
                    faq_dict[question] = answer
                    
            except Exception as e:
                print(f"Error extracting QA: {e}")
                continue
                
        return faq_dict