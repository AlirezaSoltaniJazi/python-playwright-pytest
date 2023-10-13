from playwright.sync_api import Page


class DuckDuckGoSearchPage:
    # Locators
    _SEARCH_INPUT_FIELD = '#searchbox_input'
    _SEARCH_INPUT_BUTTON = 'xpath=//button[contains(@aria-label,"Search")]'

    def __init__(self, page: Page):
        self._page = page

    def load_search_page(self, url: str) -> None:
        self._page.goto(url)

    def search_value(self, phrase: str) -> None:
        # self._page.locator(self._SEARCH_INPUT_FIELD).fill(phrase)
        self._page.fill(self._SEARCH_INPUT_FIELD, phrase)
        # self._page.locator(self._SEARCH_INPUT_BUTTON).click()
        self._page.click(self._SEARCH_INPUT_BUTTON)
