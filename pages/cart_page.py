from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage(BasePage):
    URL: str = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BUTTON: tuple = (By.ID, "checkout")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def checkout(self):
        super()._click(self.CHECKOUT_BUTTON)
