from selenium import webdriver
from selenium.webdriver.common.by import By


class RainbowPlantLifeScraper:
    def __init__(self):
        # Initialize Chrome Webdriver
        self.driver = webdriver.Chrome()
        self.driver.get("https://rainbowplantlife.com/")

    def accept_cookies(self) -> None:
        """As website uses cookies, this function accepts cookies and closes iframe window"""
        self.driver.implicitly_wait(4)
        iframe = self.driver.find_element(By.CSS_SELECTOR, " #gdpr-consent-tool-wrapper > #gdpr-consent-notice")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.ID, "save").click()


scraper = RainbowPlantLifeScraper()
scraper.accept_cookies()
