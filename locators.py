from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']") #верхняя кнопка заказа
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']") #нижняя кнопка заказа
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]") #логотип "самокат"
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]") #логотип "яндекс"
    
    #блок вопросов "вопросы о важном"
    QUESTION_1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    QUESTION_2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    QUESTION_3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTION_4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTION_5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTION_6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTION_7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTION_8 = (By.XPATH, "//div[@id='accordion__heading-7']")
    #ответы на "вопросы о важном"
    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")

#поля формы "Для кого самокат"
class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']") 
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker")  # Календарь
    DATE_PICKER_DAY = (By.CLASS_NAME, "react-datepicker__day")  # Все дни в календаре
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    
    METRO_STATION_OPTION = (By.CLASS_NAME, "select-search__row")
    METRO_STATION_BUTTON = (By.TAG_NAME, "button")
    
    RENTAL_1_DAY = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='сутки']")
    RENTAL_2_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='двое суток']")
    RENTAL_3_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='трое суток']")
    RENTAL_4_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='четверо суток']")
    RENTAL_5_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='пятеро суток']")
    RENTAL_6_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='шестеро суток']")
    RENTAL_7_DAYS = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='семеро суток']")
    
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")