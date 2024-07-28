import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import data_reader


class TestLoginPage:

    @pytest.mark.login
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(data_reader.login_username_standard, data_reader.login_password_correct)
        inventory_page = InventoryPage(driver)
        assert inventory_page.URL == inventory_page.current_url, "Actual URL is not the same as expected"

    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [(data_reader.login_username_standard, data_reader.login_password_incorrect, "Epic sadface: Username and "
                                                                                         "password do not match any "
                                                                                         "user in this service"),
                              (data_reader.login_username_lockedout, data_reader.login_password_correct, "Epic sadface: Sorry, this "
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
        login_page.login(data_reader.login_username_standard, data_reader.login_password_correct)
        inventory_page = InventoryPage(driver)
        inventory_page.logout()
        assert login_page.URL == inventory_page.current_url, "URL different than expected"
