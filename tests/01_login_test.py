import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright
from pages.loginpage import LoginPage

load_dotenv()

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        #context.storage_state(path="auth/login.json")
        browser.close()

@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto()

    login_page.login(
        os.getenv("ORANGE_USERNAME"),
        os.getenv("ORANGE_PASSWORD")
    )

    page.wait_for_selector("h6")
    assert login_page.is_login_successful(), "Login failed"