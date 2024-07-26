from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    URL: str = "https://www.saucedemo.com/inventory.html"
    ADD_BACKPACK_TO_CART_BUTTON: tuple = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK_BUTTON: tuple = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART: tuple = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_COUNTER: tuple = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BUTTON: tuple = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON: tuple = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.URL)

    def open_cart(self):
        super()._click(self.SHOPPING_CART)

    def add_or_remove_product_from_cart(self, locator: tuple):
        super()._click(locator)

    def open_menu(self):
        super()._click(self.MENU_BUTTON)

    def logout(self):
        self.open_menu()
        super()._click(self.LOGOUT_BUTTON)


