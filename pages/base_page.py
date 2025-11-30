from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
    
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )
    
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def wait_for_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
    
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def get_current_url(self):
        return self.driver.current_url
    
    def scroll_to_element(self, locator):
        #Прокрутить к элементу
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    def scroll_to_bottom(self):
        #Прокрутить вниз страницы
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")