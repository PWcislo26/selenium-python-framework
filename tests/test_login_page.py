import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLoginPage:

    @pytest.mark.login
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(login_page.USERNAME_POSITIVE, login_page.PASSWORD_POSITIVE)
        inventory_page = InventoryPage(driver)
        assert inventory_page.URL == inventory_page.current_url, "Actual URL is not the same as expected"

    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [(LoginPage.USERNAME_POSITIVE, LoginPage.PASSWORD_NEGATIVE, "Epic sadface: Username and "
                                                                                         "password do not match any "
                                                                                         "user in this service"),
                              (LoginPage.USERNAME_LOCKEDOUT, LoginPage.PASSWORD_POSITIVE, "Epic sadface: Sorry, this "
                                                                                          "user has been locked out.")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        assert login_page.get_error_message() == expected_error_message, f"Error message is different than expected {expected_error_message}"

    @pytest.mark.login
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(login_page.USERNAME_POSITIVE, login_page.PASSWORD_POSITIVE)
        inventory_page = InventoryPage(driver)
        inventory_page.logout()
        assert login_page.URL == inventory_page.current_url, "URL different than expected"
