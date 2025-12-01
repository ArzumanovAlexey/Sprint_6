import pytest
import allure
from pages.main_page import MainPage

class TestFaq:
    """Тесты для проверки вопросов и ответов на главной странице"""
    
    @allure.epic("Самокаты")
    @allure.feature("Главная страница")
    @allure.story("FAQ секция")
    @allure.title("Проверка текста в ответах на вопросы")    
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        MainPage.get_qa_data()
        )
    def test_faq_question_and_answer(self, main_page, question_locator, answer_locator, expected_text):
        """Проверка, что ответы на вопросы содержат ожидаемый текст
        
        Steps:
        1. Кликнуть на вопрос
        2. Получить текст ответа
        3. Проверить, что ответ содержит ожидаемый текст
        """
        with allure.step(f"Кликнуть на вопрос и проверить ответ содержит '{expected_text}'"):
            main_page.click_question(question_locator)
            answer_text = main_page.get_answer_text(answer_locator)

        with allure.step("Проверить, что ответ содержит ожидаемый текст"):
            assert  expected_text.lower() in answer_text.lower(), \
                f"Текст ответа '{answer_text}' не содержит '{expected_text}'"

        answer_text = main_page.get_answer_text(answer_locator)
        assert answer_text != "" and len(answer_text) > 0, "Текст ответа пустой, ожидался непустой текст"

    @allure.epic("Самокаты")
    @allure.feature("Главная страница")
    @allure.story("FAQ секция")
    @allure.title("Проверка отображения всех вопросов и ответов")
    def test_all_faq_items_have_answers(self, main_page):
        """Проверка, что у всех вопросов есть ответы
        
        Steps:
        1. Собрать все вопросы и ответы в словарь
        2. Проверить, что количество вопросов соответствует ожидаемому
        3. Проверить, что все ответы не пустые
        """      
        with allure.step("Собрать все вопросы и ответы"):
            faq_dict = main_page.qa_dictionary()

        with allure.step("Проверить количество вопросов"):
            assert len(faq_dict) == 8, f"Ожидали 8 вопросов FAQ, получили: {len(faq_dict)}"

        with allure.step("Проверить, что все ответы не пустые"):
            for question_text, answer_text in faq_dict.items():
                assert question_text.strip() != "", "Текст вопроса пустой — это не ожидается"
                assert answer_text.strip() != "", f"Пустой ответ для вопроса: '{question_text}'"