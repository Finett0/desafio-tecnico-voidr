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