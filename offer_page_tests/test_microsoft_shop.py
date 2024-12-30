from playwright.sync_api import Page, expect


def test_microsoft_shop_visibility(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_text("MicrosoftPLAY")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Microsoft")

# Add navigation to shop test
