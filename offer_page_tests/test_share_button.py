import re
from playwright.sync_api import Page, expect


def test_text_and_visibility(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_role("button", name="Share")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Share")


# def test_share_button_functionality(page: Page) -> None:
#     page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
#     expect(page.get_by_role("button", name="Copy")).to_be_visible()
#     page.get_by_role("button", name="Share").click()
#     page.get_by_role("button", name="Copy").click()