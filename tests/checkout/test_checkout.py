import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_checkout_process(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    page.click("#checkout")
    page.fill("#first-name", "Giovanni")
    page.fill("#last-name", "Finetto")
    page.fill("#postal-code", "03579240")
    page.click("#continue")
    page.click("#finish")
    assert "checkout-complete.html" in page.url