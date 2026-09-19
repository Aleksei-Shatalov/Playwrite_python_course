from playwright.sync_api import Page


# Создание скриншота всей страницы
def test_get_text(page):
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="screenshot.png", full_page=True)
