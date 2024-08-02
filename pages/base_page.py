from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_all(self, locator: tuple) -> list:
        return self._driver.find_elements(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_unit_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_unit_element_is_visible(locator, time)
        self._find(locator).click()

    def _click_all(self, locator: tuple, time: int = 10):
        self._wait_until_all_elements_are_visible(locator, time)

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_unit_element_is_visible(locator, time)
        return self._find(locator).text

    def _get_attribute(self, locator: tuple, attribute_name: str, time: int = 10) -> str:
        self._wait_unit_element_is_visible(locator, time)
        return self._find(locator).get_attribute(attribute_name)

    def _wait_unit_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_all_elements_are_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_all_elements_located(locator))

    @property
    def current_url(self) -> str:
        return self._driver.current_url
