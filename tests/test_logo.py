import time
import allure

from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка перехода по логотипу Самоката')
    def test_scooter_logo_redirect_to_main_page(self, driver):

        page = MainPage(driver)

        page.open_main_page()
        page.accept_cookies()

        page.click_scooter_logo()

        current_url = driver.current_url

        assert 'qa-scooter.praktikum-services.ru' in current_url

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirect_to_dzen(self, driver):

        page = MainPage(driver)

        page.open_main_page()
        page.accept_cookies()

        page.click_yandex_logo()

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        time.sleep(3)

        current_url = driver.current_url

        assert 'dzen.ru' in current_url