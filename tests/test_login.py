from pages.login_page import LoginPage

def test_login_valid(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_login_invalid(page):
    login = LoginPage(page)
    login.navigate()
    login.login("giovanni_finetto","quinta-Feira!")
    assert page.locator("h3[data-test='error']").is_visible()
