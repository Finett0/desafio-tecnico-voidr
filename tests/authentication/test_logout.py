import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_logout_functionality(setup):
    page = setup
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    assert "saucedemo.com" in page.url