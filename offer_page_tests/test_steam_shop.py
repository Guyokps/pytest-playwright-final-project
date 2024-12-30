from playwright.sync_api import Page, expect


def test_steam_shop_visible(page: Page) -> None:
    # Checks if steam card is visible for this page
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_text("SteamPLAY")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Steam")


# def test_steam_shop_redirect_to_correct_url(page: Page) -> None:
#     # Checks if user is redirected to the correct URL
#     page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
#     page.locator("div").filter(has_text="^SteamPLAY$").get_by_role("button").click()
