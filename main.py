import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()

    await page.goto("https://example.com")
    title = await page.title()
    print(f"Title of https://example.com: {title}")

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
