from playwright.sync_api import Page, expect


def test_play_again_button_functionality(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_role("button", name="Play again")).to_be_visible()
    page.get_by_role("button", name="Play again").click()
    expect(page).to_have_url("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc")
    expect(page.get_by_role("img").nth(4)).to_be_visible()
