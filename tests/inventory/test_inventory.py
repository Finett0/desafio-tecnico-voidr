import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory_items_count(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert inventory_page.get_inventory_items_count() > 0


def test_sort_inventory_items(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.select_option(".product_sort_container", "lohi")
    sorted_items = page.locator(".inventory_item_price").all_text_contents()
    assert sorted_items == sorted(sorted_items, key=lambda x: float(x.replace("$", "")))

def test_sort_products_a_to_z(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_products("az")
    product_names = inventory_page.get_product_names()
    sorted_names = sorted(product_names)
    assert product_names == sorted_names, "Products are not sorted correctly from A to Z"

def test_sort_products_z_to_a(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_products("za")
    product_names = inventory_page.get_product_names()
    sorted_names = sorted(product_names, reverse=True)
    assert product_names == sorted_names, "Products are not sorted correctly from Z to A"