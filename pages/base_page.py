import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.driver.get(self.MAIN_PAGE_URL)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(
                    ('id', 'rcc-confirm-button')
                )
            )
            cookie_button.click()
        except:
            pass

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    @allure.step('Кликнуть по элементу')
    def click_on_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

        ActionChains(self.driver) \
            .move_to_element(element) \
            .click() \
            .perform()

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        ).text

    @allure.step('Заполнить поле')
    def set_text_to_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        ).send_keys(text)

    @allure.step('Нажать Enter')
    def press_enter(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        ).send_keys(Keys.ENTER)