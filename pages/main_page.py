import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Кликнуть на вопрос FAQ')
    def click_faq_question(self, index):
        locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    @allure.step('Получить текст ответа FAQ')
    def get_faq_answer(self, index):
        locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )
        return self.get_text_from_element(locator)

    @allure.step('Кликнуть на верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.TOP_ORDER_BUTTON)

    @allure.step('Кликнуть на нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Кликнуть по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)    