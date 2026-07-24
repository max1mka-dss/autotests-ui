import pytest
from playwright.sync_api import sync_playwright, Playwright

@pytest.fixture

def chromium_page(playwright):
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()
