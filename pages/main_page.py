from .base_page import BasePage
from locators import MainPageLocators
from urls import MAIN_PAGE_URL


class MainPage(BasePage):
    def open(self):
        self.driver.get(MAIN_PAGE_URL)
        self.wait_for_element(MainPageLocators.ORDER_BUTTON_TOP)
        return self

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

    def click_top_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])