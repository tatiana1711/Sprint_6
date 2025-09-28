import pytest
import allure
from data import QUESTIONS_AND_ANSWERS
from pages.main_page import MainPage


class TestQuestions:
    @allure.feature('Вопросы о важном')
    @allure.story('Проверка текста ответов на вопросы')
    @pytest.mark.parametrize('question_number,expected_answer', QUESTIONS_AND_ANSWERS)
    def test_question_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        allure.dynamic.title(f"Тест вопроса №{question_number}")
        
        main_page.open()
        main_page.click_question(question_number)
        actual_answer = main_page.get_answer_text(question_number)
        
        assert actual_answer == expected_answer