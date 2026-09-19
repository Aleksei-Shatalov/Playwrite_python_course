from playwright.sync_api import Page


# Можно выполнить через 2 варианта: check() или click() — результат одинаковый. 
# отличается тем что click() просто нажимает ничего не проверяя а .check() делает проверки сначала 
# и к примеру не будет нажимать если галочка уже стоит
def test_checkbox(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()
