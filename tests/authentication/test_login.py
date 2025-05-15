import pytest
from pages.login_page import LoginPage

def test_login_valid_user(setup):
    page = setup
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url

def test_login_invalid_user(setup):
    page = setup
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("giovanni-finetto", "quinta-feira")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

def test_error_message_on_empty_login(setup):
    page = setup
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "")
    assert login_page.get_error_message() == "Epic sadface: Username is required"

def test_error_message_on_empty_password(setup):
    page = setup
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "")
    assert login_page.get_error_message() == "Epic sadface: Password is required"