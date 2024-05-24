from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


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


scraper = RainbowPlantLifeScraper()
scraper.accept_cookies()
scraper.close_ad_bar()
