from playwright.sync_api import Page

from page_object.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_name_field = self.page.locator("#username")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.get_by_text("Login")

    def navigate(self):
        self.page.goto("http://localhost:4000/login")

    def login(self, username: str, password: str):
        self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        self.page.wait_for_timeout(1000)