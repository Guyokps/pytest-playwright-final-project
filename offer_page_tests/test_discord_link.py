from playwright.sync_api import Page, expect


def test_discord_text_and_visibility(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.get_by_role("button", name="Any trouble running this game?")).to_be_visible()
    expect(page.locator("#root")).to_contain_text("Any trouble running this game?")

# This test will fail if ran in local machine that have Discord installed. should run at cloud
def test_discord_button_functionality(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    with page.expect_popup() as page2_info:
        page.get_by_role("button", name="Any trouble running this game?").click()
    page2 = page2_info.value
    page2.locator("foreignobject div").click()
    expect(page2.get_by_role("heading", name="Ludeo")).to_be_visible()
    expect(page2.locator("form")).to_contain_text("Ludeo")