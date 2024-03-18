import pytest
from playwright.sync_api import Page

from page_object.login_page import LoginPage
from page_object.workspace_page import WorkspacePage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }


@pytest.fixture
def login_page(browser) -> LoginPage:
    new_page = browser.new_page()
    login_page = LoginPage(new_page)
    login_page.navigate()
    yield login_page
    new_page.close()


@pytest.fixture
def workspace_page(browser) -> LoginPage:
    new_page = browser.new_page()
    login_page = LoginPage(new_page)
    login_page.navigate()
    login_page.login("test", "test")
    workspace_page = WorkspacePage(new_page)
    yield workspace_page
    if workspace_page.logout_button.is_visible():
        workspace_page.logout()
