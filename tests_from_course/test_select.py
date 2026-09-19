from playwright.sync_api import Page


# Выбор в выпадающем списке через select_option
def test_select(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")

    page.select_option('#skills', value=["playwright", "python"]) # множественный выбор в выпадающем списке
