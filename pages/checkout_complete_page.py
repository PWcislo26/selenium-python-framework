from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutCompletePage(BasePage):
    URL: str = "https://www.saucedemo.com/checkout-complete.html"
    THANK_YOU_TEXT_FIELD: tuple = (By.CSS_SELECTOR, "h2")
    THANK_YOU_TEXT: str = "Thank you for your order!"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def checkout_complete(self) -> bool:
        return super()._get_text(self.THANK_YOU_TEXT_FIELD) == self.THANK_YOU_TEXT
