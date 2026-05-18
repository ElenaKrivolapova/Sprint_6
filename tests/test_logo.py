import allure

from data import Urls
from pages.main_page import MainPage


class TestLogo:

    @allure.title('Проверка перехода по логотипу Самоката')
    def test_scooter_logo_redirect_to_main_page(self, driver):

        page = MainPage(driver)

        page.open_main_page()
        page.accept_cookies()

        page.click_scooter_logo()

        current_url = page.get_current_url()

        assert Urls.MAIN_PAGE_URL == current_url

    @allure.title('Проверка перехода по логотипу Яндекса')
    def test_yandex_logo_redirect_to_dzen(self, driver):

        page = MainPage(driver)

        page.open_main_page()
        page.accept_cookies()

        page.click_yandex_logo()
        page.switch_to_new_tab()
        page.wait_for_url(Urls.DZEN_URL)

        current_url = page.get_current_url()

        assert Urls.DZEN_URL in current_url