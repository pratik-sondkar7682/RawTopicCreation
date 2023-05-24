from selenium import webdriver
from pages.quotes_page import QuotePage

chrome = webdriver.Chrome("C:\\Users\\Anuja\\Desktop\\python automation\\chromedriver.exe")
chrome.get("https://quotes.toscrape.com")
page = QuotePage(chrome)
for quote in page.quotes:
    print(quote.content)
