import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import ALL_ORDER_DATA
from urls import MAIN_PAGE_URL


class TestOrder:
    @allure.feature('Заказ самоката')
    @allure.story('Позитивный сценарий заказа через верхнюю кнопку')
    @pytest.mark.parametrize('order_data', ALL_ORDER_DATA)
    def test_order_through_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        allure.dynamic.title(f"Заказ через верхнюю кнопку: {order_data['name']} {order_data['last_name']}")
        
        main_page.open()
        main_page.click_top_order_button()
        self._complete_order_flow(driver, order_data)

    @allure.feature('Заказ самоката')
    @allure.story('Позитивный сценарий заказа через нижнюю кнопку')
    @pytest.mark.parametrize('order_data', ALL_ORDER_DATA)
    def test_order_through_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        allure.dynamic.title(f"Заказ через нижнюю кнопку: {order_data['name']} {order_data['last_name']}")
        
        main_page.open()
        main_page.click_bottom_order_button()
        self._complete_order_flow(driver, order_data)

    def _complete_order_flow(self, driver, order_data):
        order_page = OrderPage(driver)
        
        order_page.fill_personal_info(
            order_data["name"],
            order_data["last_name"],
            order_data["address"],
            order_data["phone"]
        )
        
        order_page.fill_rental_info(
            order_data["period"],
            order_data["color"],
            order_data["comment"]
        )
        
        order_page.confirm_order()
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message

    @allure.feature('Навигация')
    @allure.story('Переход на главную страницу через логотип Самоката')
    def test_scooter_logo_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        assert main_page.get_current_url() == MAIN_PAGE_URL

    @allure.feature('Навигация')
    @allure.story('Переход на Дзен через логотип Яндекса')
    def test_yandex_logo_navigation(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        
        current_handles = main_page.get_window_handles()
        main_page.click_yandex_logo()
        
        main_page.wait_for_new_window(current_handles)
        original_window = main_page.get_current_window_handle()
        main_page.switch_to_new_window()
        
        main_page.wait_for_page_load()
        current_url = main_page.get_current_url()
        
        assert "dzen.ru" in current_url or "yandex.ru" in current_url
        
        main_page.close_current_window()
        main_page.switch_to_window(original_window)