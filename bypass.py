import asyncio
from pyppeteer import launch

async def preparePageForTests(page):
    # Pass the User-Agent Test.
    userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.39 Safari/537.36'
    await page.setUserAgent(userAgent)

    # Pass the Webdriver Test.
    await page.evaluateOnNewDocument("""() => {
        Object.defineProperty(navigator, 'webdriver', {
        get: () => false,
        });
    }""")

    # Pass the Chrome Test.
    await page.evaluateOnNewDocument("""() => {
        window.chrome = {
        runtime: {},
        // etc.
        };
    }""")

    # Pass the Permissions Test.
    await page.evaluateOnNewDocument("""() => {
        const originalQuery = window.navigator.permissions.query;
        return window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications' ?
            Promise.resolve({ state: Notification.permission }) :
            originalQuery(parameters)
        );
    }""")

    # Pass the Plugins Length Test.
    await page.evaluateOnNewDocument("""() => {
        // Overwrite the `plugins` property to use a custom getter.
        Object.defineProperty(navigator, 'plugins', {
        // This just needs to have `length > 0` for the current test,
        // but we could mock the plugins too if necessary.
        get: () => [1, 2, 3, 4, 5],
        });
    }""")

    # Pass the Languages Test.
    await page.evaluateOnNewDocument("""() => {
        // Overwrite the `plugins` property to use a custom getter.
        Object.defineProperty(navigator, 'languages', {
        get: () => ['zh-CN', 'zh'],
        });
    }""")


async def main():
    browser = await launch({
        'args': ['--no-sandbox'],
        'headless': True,
    })
    page = await browser.newPage()
    await preparePageForTests(page);
    await page.goto('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
