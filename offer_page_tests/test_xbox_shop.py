import re

from playwright.sync_api import Page, expect
from Locators.cloud_offer_page_locators import OfferPageLocators


def test_xbox_shop_visibility(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_text("XBoxPLAY")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("PLAY")

# Add navigation to shop
def test_xbox_shop_navigation(page: Page) -> None:
    # Workaround to avoid offer page bug
    page.goto(OfferPageLocators.hitman_url_offer_page)
    page.locator('button', has_text="Play again").click()
    page.go_back()
    print(page.url)
    page.locator("div").filter(has_text=re.compile(r"^XBoxPLAY$")).get_by_role("button").click()

    # The actual test after the workaround
    # with page.expect_popup() as page1_info:
    #     page.locator("div").filter(has_text=re.compile(r"^XBoxPLAY$")).get_by_role("button").click()
    # page1 = page1_info.value
    # expect(page1.get_by_label("Microsoft", exact=True)).to_be_visible()




