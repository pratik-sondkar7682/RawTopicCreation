from selenium.webdriver.common.by import By
from locators.quote_page_locators import QuotePageLocator
from parsers.quotes import parser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser
    @property
    def quotes(self):
        locator = QuotePageLocator.QUOTE
        quote_tag = self.browser.find_elements(By.CSS_SELECTOR,locator)
        return [parser(e) for e in quote_tag]
