from playwright.sync_api import Page
from pytest import fixture

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)


@fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)
