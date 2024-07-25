from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD: tuple = (By.ID, "user-name")
    PASSWORD_FIELD: tuple = (By.ID, "password")
    LOGIN_BUTTON: tuple = (By.ID, "login-button")
    ERROR_FIELD: tuple = (By.CSS_SELECTOR, "h3")
    USERNAME_POSITIVE: str = "standard_user"
    USERNAME_LOCKEDOUT: str = "locked_out_user"
    PASSWORD_POSITIVE: str = "secret_sauce"
    PASSWORD_NEGATIVE: str = "wrong_password"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.URL)

    def login(self, username: str, password: str):
        super()._type(self.USERNAME_FIELD, username)
        super()._type(self.PASSWORD_FIELD, password)
        super()._click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return super()._get_text(self.ERROR_FIELD)
