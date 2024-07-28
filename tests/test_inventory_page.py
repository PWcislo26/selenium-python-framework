import pytest

from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.data_reader import data_reader


class TestInventoryPage:

    @pytest.mark.inventory
    def test_add_product_to_cart(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(data_reader.login_username_standard, data_reader.login_password_correct)
        inventory_page = InventoryPage(driver)
        inventory_page.add_or_remove_product_from_cart(inventory_page.ADD_BACKPACK_TO_CART_BUTTON)
        assert inventory_page._get_text(
            inventory_page.REMOVE_BACKPACK_BUTTON) == "Remove", "Remove button is not available"
        assert inventory_page._get_text(inventory_page.SHOPPING_CART_COUNTER) == "1", "Counter has not been set to 1"

    @pytest.mark.inventory
    def test_buy_product(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(data_reader.login_username_standard, data_reader.login_password_correct)
        inventory_page = InventoryPage(driver)
        inventory_page.add_or_remove_product_from_cart(inventory_page.ADD_BACKPACK_TO_CART_BUTTON)
        inventory_page.open_cart()
        cart_page = CartPage(driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_in_checkout(data_reader.checkout_last_name, data_reader.checkout_last_name,
                                       data_reader.checkout_postal_code)
        checkout_overview_page = CheckoutOverviewPage(driver)
        checkout_overview_page.finsh_checkout()
        checkout_complete_page = CheckoutCompletePage(driver)
        assert checkout_complete_page.URL == checkout_complete_page.current_url, "ULR different than expected"
        assert checkout_complete_page.checkout_complete(), "Successful checkout message is not present"
