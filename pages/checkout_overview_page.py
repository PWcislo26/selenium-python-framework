from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutOverviewPage(BasePage):

    FINISH_BUTTON: tuple = (By.ID, "finish")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def finsh_checkout(self):
        super()._click(self.FINISH_BUTTON)
