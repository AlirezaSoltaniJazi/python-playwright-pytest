from playwright.sync_api import Page

from utils.logger_formatter import LOGGER


class DuckDuckGoResultPage:
    # Locators
    _RESULT_LINKS = 'result-title-a'
    _SEARCH_INPUT = '#search_form_input'

    def __init__(self, page: Page):
        self._page = page

    def get_link_titles(self) -> list[str]:
        # It is concatenated with the N-th element fetcher to wait for at least 5 elements to appear
        self._page.get_by_test_id(self._RESULT_LINKS).nth(5).wait_for()
        titles = self._page.get_by_test_id(self._RESULT_LINKS).all_text_contents()
        LOGGER.info('Result Titles', extra={'Titles': titles})
        return titles

    def get_search_input_text(self) -> str:
        search_input_text = self._page.input_value(self._SEARCH_INPUT)
        LOGGER.info('Search Input Data', extra={'Text': search_input_text})
        return search_input_text

    def get_page_title(self) -> str:
        page_title = self._page.title()
        LOGGER.info('Page Title', extra={'Title': page_title})
        return page_title
