from playwright.sync_api import sync_playwright,expect,Page
import pytest
from pages.login_page import LoginPage
@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email:str, password: str):

        #login_page = LoginPage(page=chromium_page)
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.fill_login_form(email=email, password=password )
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()



        #
        # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        #
        # # email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        # email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        #
        # email_input.fill('user.name@gmail.com')
        #
        # # password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        # password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        # password_input.fill('password')
        #
        # # login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        # # login_button.click()
        # login_button = chromium_page.get_by_test_id('login-page-login-button')
        # login_button.click()
        #
        # # wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        # wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        # expect(wrong_email_or_password_alert).to_be_visible()
        # expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')

