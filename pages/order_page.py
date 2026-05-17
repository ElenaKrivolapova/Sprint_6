import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнить поле Имя')
    def set_name(self, name):
        self.set_text_to_element(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Заполнить поле Фамилия')
    def set_surname(self, surname):
        self.set_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Заполнить поле Адрес')
    def set_address(self, address):
        self.set_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбрать станцию метро')
    def select_metro_station(self, metro):
        self.set_text_to_element(OrderPageLocators.METRO_INPUT, metro)
        metro_option_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(metro)
        )
        self.click_on_element(metro_option_locator)

    @allure.step('Заполнить поле Телефон')
    def set_phone(self, phone):
        self.set_text_to_element(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить первую форму заказа')
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.select_metro_station(metro)
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Заполнить дату доставки')
    def set_delivery_date(self, date):
        self.set_text_to_element(OrderPageLocators.DATE_INPUT, date)
        self.press_enter(OrderPageLocators.DATE_INPUT)

    @allure.step('Выбрать срок аренды')
    def select_rent_period(self, period):
        self.click_on_element(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        period_option_locator = (
            OrderPageLocators.RENT_PERIOD_OPTION[0],
            OrderPageLocators.RENT_PERIOD_OPTION[1].format(period)
        )
        self.click_on_element(period_option_locator)

    @allure.step('Выбрать цвет самоката')
    def select_scooter_color(self, color):
        if color == 'black':
            self.click_on_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        else:
            self.click_on_element(OrderPageLocators.GREY_COLOR_CHECKBOX)

    @allure.step('Заполнить комментарий для курьера')
    def set_comment(self, comment):
        self.set_text_to_element(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Заполнить вторую форму заказа')
    def fill_second_order_form(self, date, period, color, comment):
        self.set_delivery_date(date)
        self.select_rent_period(period)
        self.select_scooter_color(color)
        self.set_comment(comment)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Получить текст об успешном создании заказа')
    def get_success_order_text(self):
        return self.get_text_from_element(OrderPageLocators.SUCCESS_ORDER_TEXT)