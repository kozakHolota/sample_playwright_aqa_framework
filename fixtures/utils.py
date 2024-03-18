import pathlib

import pandas
import pytest
from playwright.sync_api import Page

from fixtures.pages import workspace_page
from page_object.workspace_page import WorkspacePage


@pytest.fixture
def create_contacts_and_get_updates(workspace_page: WorkspacePage) -> tuple[WorkspacePage, list[dict]]:
    contacts_to_create = pandas.read_csv(pathlib.Path("params/create_contacts.csv"), sep=";", header=0).to_dict(
        orient="records")
    contacts_to_update = pandas.read_csv(pathlib.Path("params/update_contacts.csv"), sep=";", header=0).to_dict(
        orient="records")
    for contact in contacts_to_create:
        workspace_page.create_contact(**contact)
    yield workspace_page, contacts_to_update


@pytest.fixture
def create_contacts(workspace_page: WorkspacePage) -> WorkspacePage:
    contacts_to_create = pandas.read_csv(pathlib.Path("params/create_contacts.csv"), sep=";", header=0).to_dict(
        orient="records")
    for contact in contacts_to_create:
        workspace_page.create_contact(**contact)
    yield workspace_page


@pytest.fixture
def delete_contacts(page: Page):
    yield
    workspace_page = WorkspacePage(page)
    workspace_page.delete_all_contacts()


@pytest.fixture(scope="session", autouse=True)
def run_server():
    import subprocess
    process = subprocess.Popen(["npm", "run", "dev"], cwd=pathlib.Path("qa_task"), stdout=subprocess.PIPE,  )
    yield
    process.terminate()
