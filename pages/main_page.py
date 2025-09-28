from .base_page import BasePage
from locators import MainPageLocators
from urls import MAIN_PAGE_URL
import allure


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(MAIN_PAGE_URL)
        self.wait_for_element(MainPageLocators.ORDER_BUTTON_TOP)
        return self

    @allure.step("Нажать на вопрос номер {question_number}")
    def click_question(self, question_number):
        question_locators = {
            1: MainPageLocators.QUESTION_1,
            2: MainPageLocators.QUESTION_2,
            3: MainPageLocators.QUESTION_3,
            4: MainPageLocators.QUESTION_4,
            5: MainPageLocators.QUESTION_5,
            6: MainPageLocators.QUESTION_6,
            7: MainPageLocators.QUESTION_7,
            8: MainPageLocators.QUESTION_8
        }
        self.scroll_to_element(question_locators[question_number])
        self.click_element(question_locators[question_number])

    @allure.step("Получить текст ответа для вопроса {question_number}")
    def get_answer_text(self, question_number):
        answer_locators = {
            1: MainPageLocators.ANSWER_1,
            2: MainPageLocators.ANSWER_2,
            3: MainPageLocators.ANSWER_3,
            4: MainPageLocators.ANSWER_4,
            5: MainPageLocators.ANSWER_5,
            6: MainPageLocators.ANSWER_6,
            7: MainPageLocators.ANSWER_7,
            8: MainPageLocators.ANSWER_8
        }
        return self.get_text(answer_locators[question_number])

    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        current_handle = self.get_current_window_handle()
        all_handles = self.get_window_handles()
        
        for handle in all_handles:
            if handle != current_handle:
                self.switch_to_window(handle)
                return