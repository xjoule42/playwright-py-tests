from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page):
        self.page: Page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button[type="submit"]')

    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def is_login_successful(self):
        return self.page.locator("h6").inner_text() == "Dashboard"