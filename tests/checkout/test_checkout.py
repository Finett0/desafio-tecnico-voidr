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


def test_checkout_required_fields(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    page.click("#checkout")
    page.click("#continue")
    error_message = page.text_content("[data-test='error']")
    assert "Error: First Name is required" in error_message
    page.fill("#first-name", "Giovanni")
    page.click("#continue")
    error_message = page.text_content("[data-test='error']")
    assert "Error: Last Name is required" in error_message
    page.fill("#last-name", "Finetto")
    page.click("#continue")
    error_message = page.text_content("[data-test='error']")
    assert "Error: Postal Code is required" in error_message


def test_checkout_success_message(setup):
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
    success_header = page.text_content(".complete-header")
    assert "Thank you for your order!" in success_header
    assert page.is_visible("#back-to-products")