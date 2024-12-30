from playwright.sync_api import Page, expect


def test_texts_visibility(page: Page) -> None:
    page.goto("https://playable.ludeo.com/8774c270-e3b0-4ef2-ae32-5fda703574bc/offer")
    expect(page.locator("img").first).to_be_visible()
    expect(page.get_by_role("heading", name="Enjoyed this playable moment?")).to_be_visible()
    expect(page.get_by_role("heading", name="PLAY FOR FREE NOW ON")).to_be_visible()

