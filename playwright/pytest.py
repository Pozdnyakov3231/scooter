import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True,snapshots=True, sources=True)
    page = context.new_page()
    page.goto("http://localhost:8000/admin/login/?next=/admin/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("admin")
    page.get_by_role("textbox", name="Username:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("admin")
    page.get_by_role("textbox", name="Password:").press("Enter")
    page.goto("http://localhost:8000/polls/")
    page.goto("http://localhost:8000/nocodb-data/")

    # ---------------------
    context.tracing.stop(path = "trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
