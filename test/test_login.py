import pytest
from playwright.sync_api import expect

from page_object.login_page import LoginPage
from page_object.workspace_page import WorkspacePage


@pytest.mark.login_actions
@pytest.mark.login
def test_login(login_page: LoginPage, username, password, expected_text):
    """Verify user login process"""
    login_page.login(username, password)
    expect(login_page.page_body).to_have_text(expected_text, timeout=1000)

@pytest.mark.smoke
@pytest.mark.login_actions
@pytest.mark.logout
def test_logout(workspace_page: WorkspacePage):
    """Verify user logout process"""
    login_page: LoginPage = workspace_page.logout()
    expect(login_page.user_name_field).to_be_visible()
    expect(login_page.password_field).to_be_visible()
    expect(login_page.login_button).to_be_visible()
