import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize('order_button', ['top', 'bottom'])
    @pytest.mark.parametrize(
        'name, surname, address, metro, phone, date, period, color, comment',
        [
            [
                'Елена',
                'Иванова',
                'Москва, улица Пушкина, дом 1',
                'Сокольники',
                '+79999999999',
                '20.05.2026',
                'сутки',
                'black',
                'Позвонить за час'
            ],
            [
                'Анна',
                'Петрова',
                'Москва, улица Ленина, дом 2',
                'Черкизовская',
                '+78888888888',
                '21.05.2026',
                'двое суток',
                'grey',
                'Оставить у подъезда'
            ]
        ]
    )
    @allure.title('Проверка позитивного сценария заказа самоката')
    def test_create_order_success(
            self,
            driver,
            order_button,
            name,
            surname,
            address,
            metro,
            phone,
            date,
            period,
            color,
            comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.accept_cookies()

        if order_button == 'top':
            main_page.click_top_order_button()
        else:
            main_page.click_bottom_order_button()

        order_page.fill_first_order_form(name, surname, address, metro, phone)
        order_page.fill_second_order_form(date, period, color, comment)
        order_page.confirm_order()

        success_text = order_page.get_success_order_text()

        assert 'Заказ оформлен' in success_text