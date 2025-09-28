from .base_page import BasePage
from locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    @allure.step("Заполнить личную информацию: имя '{name}', фамилия '{last_name}', адрес '{address}', телефон '{phone}'")
    def fill_personal_info(self, name, last_name, address, phone):
        self.wait_for_element(OrderPageLocators.NAME_INPUT)
        
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        
        self._select_metro_station()
        
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать станцию метро")
    def _select_metro_station(self):
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        self.wait_for_element(OrderPageLocators.METRO_STATION_OPTION)
        
        metro_options = self.wait_for_elements(OrderPageLocators.METRO_STATION_OPTION)
        if metro_options:
            first_button = metro_options[0].find_element(*OrderPageLocators.METRO_STATION_BUTTON)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", first_button)
            first_button.click()

    @allure.step("Заполнить информацию об аренде: период '{period}', цвет '{color}', комментарий '{comment}'")
    def fill_rental_info(self, period, color, comment):
        self.wait_for_element(OrderPageLocators.DATE_INPUT)
        
        self._handle_date_field()
        
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        
        period_locators = {
            "сутки": OrderPageLocators.RENTAL_1_DAY,
            "двое суток": OrderPageLocators.RENTAL_2_DAYS,
            "трое суток": OrderPageLocators.RENTAL_3_DAYS,
            "четверо суток": OrderPageLocators.RENTAL_4_DAYS,
            "пятеро суток": OrderPageLocators.RENTAL_5_DAYS,
            "шестеро суток": OrderPageLocators.RENTAL_6_DAYS,
            "семеро суток": OrderPageLocators.RENTAL_7_DAYS
        }
        
        self.wait_for_element(period_locators[period])
        self.click_element(period_locators[period])
        
        if color:
            color_locators = {
                "black": OrderPageLocators.COLOR_BLACK,
                "grey": OrderPageLocators.COLOR_GREY
            }
            self.click_element(color_locators[color])
        
        if comment:
            self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Обработать поле даты")
    def _handle_date_field(self):
        self.click_element(OrderPageLocators.DATE_INPUT)
        
        if self.is_element_present(OrderPageLocators.DATE_PICKER, timeout=3):
            available_days = self.wait_for_elements(OrderPageLocators.DATE_PICKER_DAY)
            if available_days:
                available_days[0].click()
            else:
                self._close_calendar()
        else:
            self._close_calendar()

    @allure.step("Закрыть календарь")
    def _close_calendar(self):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.wait_for_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        self.wait_for_element(OrderPageLocators.SUCCESS_MESSAGE, timeout=20)
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)