import pytest
import allure
from pages.main_page import MainPage
from helpers.test_data_generator import get_qa_data

@allure.epic("Самокаты")
@allure.feature("Главная страница")
@allure.story("FAQ секция")
class TestFaq:

    @pytest.mark.parametrize("index", range(len(get_qa_data())))
    @allure.title("FAQ: проверка вопроса №{index}")
    def test_faq_question_and_answer(self, main_page, index):
        """
        Проверка FAQ: каждый вопрос и ответ — отдельный параметр
        """

        qa_data = get_qa_data()
        question_locator, answer_locator, expected_text = qa_data[index]

        with allure.step(f"Кликаем на вопрос №{index}"):
            main_page.click_question(question_locator)

        with allure.step("Получаем текст ответа"):
            actual_text = main_page.get_answer_text(answer_locator)

        with allure.step("Проверяем, что ответ содержит ожидаемый текст"):
            assert expected_text.lower() in actual_text.lower(), \
                f"Ожидаемый текст '{expected_text}' не найден в ответе '{actual_text}'"
