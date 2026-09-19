from playwright.sync_api import Page


# Загрузка файла
def test_select_multiple(page):
    page.goto('https://zimaev.github.io/upload/', wait_until='domcontentloaded')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()


# Другой вариант через регистрацию обработчика события "filechooser"
def test_select_multiple_2(page):
    page.goto('https://zimaev.github.io/upload/', wait_until='domcontentloaded')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#formFile").click()
