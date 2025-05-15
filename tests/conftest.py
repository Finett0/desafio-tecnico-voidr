import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup(playwright):
    browser = playwright.chromiun.lanch(headless=False,slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

