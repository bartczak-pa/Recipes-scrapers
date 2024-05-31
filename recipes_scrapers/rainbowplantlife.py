from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, ParseResult


class RainbowPlantLifeScraper:
    def __init__(self):
        # Initialize Chrome Webdriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://rainbowplantlife.com/")
        self.driver.implicitly_wait(4)

    def accept_cookies(self) -> None:
        """As website uses cookies, this function accepts cookies and closes iframe window"""

        try:
            iframe = self.driver.find_element(By.CSS_SELECTOR, " #gdpr-consent-tool-wrapper > #gdpr-consent-notice")
            self.driver.switch_to.frame(iframe)
            self.driver.find_element(By.ID, "save").click()
        except NoSuchElementException:
            print("Cookies already accepted or window with cookies not visible")

    def close_ad_bar(self) -> None:
        """Helper function closing ad bar, otherwise button 'Load more recipes' will be not available to click for the
        Selenium"""
        self.driver.find_element(By.CLASS_NAME, "adthrive-close").click()

    def parse_categories(self) -> dict:
        """Parse categories and their URL's from the website"""
        categories: dict = {}

        for category in self.driver.find_elements(By.CSS_SELECTOR, "#menu-item-116 .sub-menu li > a"):
            link: str = category.get_attribute("href")

            # While using selenium .text method is not working properly, so we need to parse title from the URL
            parsed_url: ParseResult = urlparse(link)
            title: str = parsed_url.path.split('/')[-2].replace('-', ' ').title()
            categories[title] = link

        return categories


scraper = RainbowPlantLifeScraper()
scraper.accept_cookies()
scraper.close_ad_bar()
categories = scraper.parse_categories()

