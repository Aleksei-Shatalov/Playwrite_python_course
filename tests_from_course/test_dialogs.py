from playwright.sync_api import Page


# Диалоговые окна
def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()
