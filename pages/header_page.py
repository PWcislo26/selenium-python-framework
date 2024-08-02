from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class HeaderPage(BasePage):

    MENU_BUTTON: tuple = (By.ID, "react-burger-menu-btn")
    MENU_BUTTON_WRAP: tuple = (By.CLASS_NAME, "bm-menu-wrap")
    LOGOUT_BUTTON: tuple = (By.ID, "logout_sidebar_link")
    SHOPPING_CART: tuple = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_COUNTER: tuple = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _check_if_menu_is_opened(self) -> bool:
        is_hidden = super()._get_attribute(self.MENU_BUTTON_WRAP, "aria-hidden")
        if is_hidden == "true":
            return False
        return True

    def open_menu(self):
        if not self._check_if_menu_is_opened():
            super()._click(self.MENU_BUTTON)

    def open_cart(self):
        super()._click(self.SHOPPING_CART)

    def logout(self):
        self.open_menu()
        super()._click(self.LOGOUT_BUTTON)




