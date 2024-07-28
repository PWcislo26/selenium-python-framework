from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage(BasePage):
    CONTINUE_BUTTON: tuple = (By.ID, "continue")
    FIRST_NAME_FIELD: tuple = (By.ID, "first-name")
    LAST_NAME_FIELD: tuple = (By.ID, "last-name")
    POSTAL_CODE_FIELD: tuple = (By.ID, "postal-code")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def fill_in_checkout(self, firstname: str, lastname: str, postalcode: str):
        super()._type(self.FIRST_NAME_FIELD, firstname)
        super()._type(self.LAST_NAME_FIELD, lastname)
        super()._type(self.POSTAL_CODE_FIELD, postalcode)
        super()._click(self.CONTINUE_BUTTON)
