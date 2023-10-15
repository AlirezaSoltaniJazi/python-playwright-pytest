from playwright.sync_api import Page, sync_playwright, Browser, BrowserContext
from pytest import fixture

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)


# Create Customize browser instance
@fixture(scope='session')
def browser(config):
    browser_config = config['config']
    headless_mode_config = config['active_headless_mode']
    playwright = sync_playwright()
    browsers = {
        "chrome": playwright.start().chromium,
        "firefox": playwright.start().firefox,
        "webkit": playwright.start().webkit
    }
    browser_args = {
        "headless": False
    }
    if browser_config == 'webkit' and headless_mode_config:
        browser_instance = browsers['webkit'].launch(**browser_args)
    elif browser_config == 'webkit':
        browser_instance = browsers['webkit'].launch()
    elif browser_config == 'firefox' and headless_mode_config:
        browser_instance = browsers['firefox'].launch(**browser_args)
    elif browser_config == 'firefox':
        browser_instance = browsers['firefox'].launch()
    elif browser_config == 'chrome' and headless_mode_config:
        browser_instance = browsers['chrome'].launch(**browser_args)
    else:
        browser_instance = browsers['chrome'].launch()
    yield browser_instance
    browser_instance.close()


@fixture
def context(browser: Browser):
    context_instance = browser.new_context()
    return context_instance


@fixture
def page(context: BrowserContext):
    page_instance = context.new_page()
    yield page_instance
    page_instance.close()
