from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.config import Config


class BasePage:
    """Базовый класс с общими методами для работы со страницами"""
    
    def __init__(self, driver):
        """Инициализация базового класса"""
        self.driver = driver
        self.timeout = Config.TIMEOUT
        self.wait = WebDriverWait(driver, self.timeout)

    
    
    
    def find_element(self, locator):
        """Поиск элемента с ожиданием его видимости"""       
        try:
            element =self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"Элемент {locator} не найден за отведенное время")
            return None
    
    def find_elements(self, locator):
        """Поиск всех элементов по локатору"""        
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            print(f"Элементы {locator} не найдены за отведенное время")
            return []
       
    def execute_script(self, script, *args):
        """Выполнение JavaScript кода"""
        return self.driver.execute_script(script, *args)
    
    def scroll_to_element(self, locator):
        """Скролл к указанному элементу"""     
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)
    
    def scroll_to_bottom(self):
        """Скролл до нижней части страницы"""
        self.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    def scroll_to_element_center(self, element):
        """Скролл к элементу с центрированием"""
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def click_element_via_script(self, element):
        """Клик по элементу через JavaScript"""
        self.execute_script("arguments[0].click();", element)
    
    def input_text(self, locator, text):
        """Ввод текста в поле"""   
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def click(self, locator):
        """Клик по элементу со скроллом и ожиданием кликабельности"""   
        try:
            self.scroll_to_element(locator)
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            print(f"Элемент {locator} не найден за отведенное время")
            
    def get_current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url
    
    def check_page_url(self, page):
        """Проверяет URL страницы"""
        match page:
            case 'main_page':
                self.wait.until(EC.url_matches(f"^{Config.BASE_URL}.*"))
                return self.get_current_url()
            case 'order_page':
                self.wait.until(EC.url_contains(Config.ORDER_PAGE_URL))
                return self.get_current_url()
            case 'dzen_page':
                self.wait.until(EC.url_contains("dzen"))
                return self.get_current_url()
            case _:
                raise ValueError(f"Страница: {page} не найдена")
    
    def get_current_window_handle(self):
        """Получить handle текущего окна"""
        return self.driver.current_window_handle
    
    def get_window_handles(self):
        """Получить все handles окон"""
        return self.driver.window_handles
    
    def switch_to_window(self, window_handle):
        """Переключиться на указанное окно"""
        self.driver.switch_to.window(window_handle)
    
    def switch_new_window(self):
        """Выполнить переход на другую вкладку в браузере"""
        original_window = self.get_current_window_handle()
        # Ждем появления нового окна
        self.wait.until(EC.number_of_windows_to_be(2))
        # Находим новое окно
        for window_handle in self.get_window_handles():
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                return window_handle
        raise Exception("Новое окно не найдено")
    