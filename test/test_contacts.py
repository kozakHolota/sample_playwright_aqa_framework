import pytest
from playwright.sync_api import expect

from page_object.workspace_page import WorkspacePage


@pytest.mark.contacts
@pytest.mark.create_contacts
def test_create_contact(workspace_page: WorkspacePage, delete_contacts, first_name, last_name, twitter,
                        avatar_url, notes):
    """Verify user can create a contact"""
    workspace_page.create_contact(first_name, last_name, twitter, avatar_url, notes)
    expect(workspace_page.get_current_contact_locator(first_name, last_name)).to_be_visible()

    workspace_page.get_contact(first_name, last_name)
    expect(workspace_page.first_name_field).to_have_value(first_name)
    expect(workspace_page.last_name_field).to_have_value(last_name)
    expect(workspace_page.twitter_field).to_have_value(twitter)
    expect(workspace_page.avatar_url_field).to_have_value(avatar_url)
    expect(workspace_page.notes_field).to_have_value(notes)


@pytest.mark.smoke
@pytest.mark.contacts
@pytest.mark.create_invalid_contact
def test_create_contact_without_identification(workspace_page: WorkspacePage, delete_contacts):
    """Verify user cannot create a contact without identification"""
    first_name = ""
    last_name = ""
    twitter = "@bubka"
    avatar_url = "https://www.johndoe.com"
    notes = "testing"
    workspace_page.create_contact(first_name, last_name, twitter, avatar_url, notes)
    expect(workspace_page.contacts).to_be_empty()


@pytest.mark.smoke
@pytest.mark.contacts
@pytest.mark.cancel_create_contact
def test_cancel_create_contact(workspace_page: WorkspacePage, delete_contacts):
    """Verify user can cancel creating a contact"""
    first_name = "John"
    last_name = "Doe"
    twitter = "@johndoe"
    avatar_url = "https://www.johndoe.com"
    notes = "notes"
    workspace_page.create_contact(first_name, last_name, twitter, avatar_url, notes, save_contact=False)
    expect(workspace_page.get_current_contact_locator(first_name, last_name)).to_be_empty()


@pytest.mark.smoke
@pytest.mark.contacts
def test_favorize_contact(workspace_page: WorkspacePage, delete_contacts):
    """Verify user can favorize a contact"""
    first_name = "John"
    last_name = "Doe"
    twitter = "@johndoe"
    avatar_url = "https://www.johndoe.com"
    notes = "notes"
    workspace_page.create_contact(first_name, last_name, twitter, avatar_url, notes)
    assert not workspace_page.is_contact_favorized, "Favorize button should not be checked"
    workspace_page.favorize_contact()
    assert workspace_page.is_contact_favorized, "Favorize button should be checked"


@pytest.mark.contacts
@pytest.mark.update_contacts
def test_update_contact(create_contacts_and_get_updates, delete_contacts):
    """Verify user can update a contact"""
    workspace_page, contacts_to_update = create_contacts_and_get_updates
    for contact in contacts_to_update:
        workspace_page.update_contact(**contact)

    for contact in contacts_to_update:
        workspace_page.get_contact(contact["first_name"], contact["last_name"])
        expect(workspace_page.first_name_field).to_have_value(contact["first_name"], timeout=500)
        expect(workspace_page.last_name_field).to_have_value(contact["last_name"], timeout=500)
        expect(workspace_page.twitter_field).to_have_value(contact["twitter"], timeout=500)
        expect(workspace_page.avatar_url_field).to_have_value(contact["avatar_url"], timeout=500)
        expect(workspace_page.notes_field).to_have_value(contact["notes"], timeout=500)


@pytest.mark.smoke
@pytest.mark.contacts
@pytest.mark.filter_contacts
def test_filter_contacts(create_contacts: WorkspacePage):
    """Verify user can filter contacts"""
    query = "Jane Doe"
    create_contacts.filter_contacts(query)
    contacts = create_contacts.contacts
    expect(contacts).to_have_count(2)
