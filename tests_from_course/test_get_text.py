from playwright.sync_api import Page


# Получение значений элемента с помощью all_inner_text() и all_text_contents()
# Разница: all_inner_text() убирает пробелы, а all_text_contents() оставляет 
def test_get_text(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_inner_texts())


def test_get_text2(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print(row.all_text_contents())
