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


def test_correct_item(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    product_name = page.locator(".inventory_item_name").first.text_content()
    inventory_page.add_item_to_cart(0)
    inventory_page.go_to_cart()
    cart_product_name = page.locator(".inventory_item_name").first.text_content()
    assert product_name == cart_product_name

# No seu arquivo test_cart.py, modifique o teste test_add_multiple_items_to_cart
def test_add_multiple_items_to_cart(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    page.wait_for_selector("#login-button", state="visible")
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_selector(".inventory_container", state="visible")
    inventory_page.add_item_to_cart(0)
    inventory_page.add_item_to_cart(1)
    inventory_page.add_item_to_cart(2)
    page.wait_for_selector(".shopping_cart_badge", state="visible")
    cart_count = page.text_content(".shopping_cart_badge")
    assert cart_count == "3"
    inventory_page.go_to_cart()
    page.wait_for_selector(".cart_list", state="visible")
    assert "cart.html" in page.url
    assert page.locator(".cart_item").count() == 3

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
