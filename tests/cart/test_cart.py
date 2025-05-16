import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_cart_icon(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    cart_count = page.text_content(".shopping_cart_badge")
    assert cart_count == "1"


def test_add_item_to_cart(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    assert "cart.html" in page.url

def test_add_multiple_items_to_cart(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    inventory_page.add_item_to_cart(1)
    inventory_page.add_item_to_cart(2)
    inventory_page.go_to_cart()
    assert "cart.html" in page.url


def test_cart_remove_item(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    page.click(".cart_button") 
    assert page.locator(".cart_item").count() == 0