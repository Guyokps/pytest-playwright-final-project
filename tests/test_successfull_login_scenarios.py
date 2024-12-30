from playwright.sync_api import Page, expect
import pytest
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

standard_user_id = os.getenv('standard_user_id')
general_pw = os.getenv('general_pw')

test_date = [
    (standard_user_id, general_pw),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
]


@pytest.mark.parametrize("username, password", test_date)
def test_valid_login_scenarios(page: Page, username: str, password: str) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html', timeout=8000)
    expect(page.locator('[data-test="title"]')).to_contain_text('Product')
