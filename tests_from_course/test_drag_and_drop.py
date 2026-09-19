from playwright.sync_api import Page


# Тест на Drag and Drop
def test_drag_and_drop(page: Page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")
