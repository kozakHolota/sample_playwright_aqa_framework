from playwright.async_api import Page

from page_object.base_page import BasePage
from page_object.login_page import LoginPage


class WorkspacePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.filter_search = self.page.locator("#query")
        self.new_contact_button = self.page.get_by_test_id("new-contact")
        self.first_name_field = self.page.get_by_test_id("first")
        self.last_name_field = self.page.get_by_test_id("last")
        self.twitter_field = self.page.get_by_test_id("twitter")
        self.avatar_url_field = self.page.get_by_test_id("avatar")
        self.notes_field = self.page.get_by_test_id("notes")
        self.favorize_button = self.page.get_by_test_id("favorize-contact")
        self.save_button = self.page.get_by_test_id("save-contact")
        self.cancel_button = self.page.get_by_test_id("cancel-contact")
        self.logout_button = self.page.get_by_test_id("signout")

        self.favorized_contact_value = "★"
        self.unfavorized_contact_value = "☆"

    @property
    def contacts(self):
        return self.page.locator("nav a")

    @property
    def is_contact_favorized(self):
        favorized_value = self.favorize_button.text_content()
        return True if favorized_value == self.favorized_contact_value else False

    def navigate(self):
        raise NotImplementedError("navigate method is not implemented")

    def filter_contacts(self, query: str):
        self.filter_search.fill(query)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)

    def favorize_contact(self):
        self.favorize_button.click()
        self.page.wait_for_timeout(1000)

    def unfavorize_contact(self):
        self.favorize_button.click()
        self.page.wait_for_timeout(1000)

    def edit_contact(self, first_name: str, last_name: str, twitter: str, avatar_url: str, notes: str,
                           save_contact: bool = True, replace_same=False):
        if replace_same:
            existing_first_name = self.first_name_field.get_attribute("value")
            existing_last_name = self.last_name_field.get_attribute("value")
            existing_twitter = self.twitter_field.get_attribute("value")
            existing_avatar_url = self.avatar_url_field.get_attribute("value")
            existing_notes = self.notes_field.get_attribute("value")
            if existing_first_name != first_name:
                self.first_name_field.fill(first_name)
            if existing_last_name != last_name:
                self.last_name_field.fill(last_name)
            if existing_twitter != twitter:
                self.twitter_field.fill(twitter)
            if existing_avatar_url != avatar_url:
                self.avatar_url_field.fill(avatar_url)
            if existing_notes != notes:
                self.notes_field.fill(notes)
        else:
            self.first_name_field.fill(first_name)
            self.last_name_field.fill(last_name)
            self.twitter_field.fill(twitter)
            self.avatar_url_field.fill(avatar_url)
            self.notes_field.fill(notes)

        if save_contact:
            self.save_button.click()
        else:
            self.cancel_button.click()

    def create_contact(self, first_name: str, last_name: str, twitter: str, avatar_url: str, notes: str,
                             save_contact: bool = True):
        self.new_contact_button.click()
        self.edit_contact(first_name, last_name, twitter, avatar_url, notes, save_contact=save_contact)

    def update_contact(self, first_name: str, last_name: str, twitter: str, avatar_url: str, notes: str,
                             save_contact: bool = True):
        edit_button = self.page.get_by_test_id("edit-contact")
        edit_button.click()
        self.edit_contact(first_name, last_name, twitter, avatar_url, notes, save_contact=save_contact)

    def get_current_contact_locator(self, first_name: str, last_name: str):
        return self.page.locator(f"//a[contains(text(), '{first_name if first_name else last_name}')]")

    def get_contact(self, first_name: str, last_name: str):
        self.get_current_contact_locator(first_name, last_name).click(timeout=1000)
        self.page.wait_for_timeout(1000)

    def delete_current_contact(self):
        delete_button = self.page.get_by_test_id("delete-contact")
        delete_button.click()
        self.accept_dialog()

        self.page.wait_for_timeout(1000)

    def delete_contact(self, first_name: str, last_name: str):
        self.get_contact(first_name, last_name)
        self.delete_current_contact()

    def delete_all_contacts(self):
        for contact in self.contacts.all():
            contact.click()
            self.delete_current_contact()

    def logout(self):
        self.logout_button.click()
        self.page.wait_for_timeout(1000)
        return LoginPage(self.page)
