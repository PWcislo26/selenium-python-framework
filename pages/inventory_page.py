from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header_page import HeaderPage


class InventoryPage(HeaderPage):

    URL: str = "https://www.saucedemo.com/inventory.html"
    ADD_BACKPACK_TO_CART_BUTTON: tuple = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON: tuple = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.URL)

    def add_or_remove_product_from_cart(self, locator: tuple):
        super()._click(locator)

