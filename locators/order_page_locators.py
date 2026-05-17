from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Имя']"
    )

    SURNAME_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Фамилия']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Адрес: куда привезти заказ']"
    )

    METRO_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Станция метро']"
    )

    METRO_OPTION = (
        By.XPATH,
        ".//div[text()='{}']"
    )

    PHONE_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        ".//button[text()='Далее']"
    )

    DATE_INPUT = (
        By.XPATH,
        ".//input[@placeholder='* Когда привезти самокат']"
    )

    RENT_PERIOD_DROPDOWN = (
        By.CLASS_NAME,
        'Dropdown-placeholder'
    )

    RENT_PERIOD_OPTION = (
        By.XPATH,
        ".//div[text()='{}']"
    )

    BLACK_COLOR_CHECKBOX = (
        By.ID,
        'black'
    )

    GREY_COLOR_CHECKBOX = (
        By.ID,
        'grey'
    )

    COMMENT_INPUT = (
        By.XPATH,
        ".//input[@placeholder='Комментарий для курьера']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    )

    YES_BUTTON = (
        By.XPATH,
        ".//button[text()='Да']"
    )

    SUCCESS_ORDER_TEXT = (
        By.XPATH,
        ".//div[contains(@class, 'Order_ModalHeader')]"
    )