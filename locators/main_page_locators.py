from selenium.webdriver.common.by import By


class MainPageLocators:

    FAQ_QUESTION = (
        By.ID,
        'accordion__heading-{}'
    )

    FAQ_ANSWER = (
        By.ID,
        'accordion__panel-{}'
    )

    TOP_ORDER_BUTTON = (
        By.XPATH,
        ".//button[text()='Заказать']"
    )

    BOTTOM_ORDER_BUTTON = (
        By.CLASS_NAME,
        'Button_Middle__1CSJM'
    )

    SCOOTER_LOGO = (
        By.CLASS_NAME,
        'Header_LogoScooter__3lsAR'
    )

    YANDEX_LOGO = (
        By.CLASS_NAME,
        'Header_LogoYandex__3TSOI'
    )