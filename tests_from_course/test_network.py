from playwright.sync_api import Page


def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://web.archive.org/web/20240623032910/https://reqres.in/', wait_until='domcontentloaded')
    page.get_by_text(' Register - successful ').click()
