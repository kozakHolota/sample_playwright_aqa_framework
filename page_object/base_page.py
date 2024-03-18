from abc import ABC

from playwright.sync_api import Page


def abstratmethod(args):
    pass


class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page
        self.page_body = self.page.locator("body")

    def dismiss_dialog_function(self, dialog):
        dialog.dismiss()

    async def dismiss_dialog(self, dialog):
        self.page.on("dialog", self.dismiss_dialog_function)

    def accept_dialog_function(self, dialog):
        dialog.accept()

    def accept_dialog(self):
        self.page.on("dialog", self.accept_dialog_function)

    @abstratmethod
    def navigate(self):
        raise NotImplementedError("navigate method is not implemented")