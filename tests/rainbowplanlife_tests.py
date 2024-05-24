from unittest.mock import MagicMock, patch, call
from recipes_scrapers import rainbowplantlife


@patch('selenium.webdriver.Chrome')
def test_accept_cookies(mock_driver):
    # Create mock objects for the elements
    mock_iframe = MagicMock()
    mock_save_button = MagicMock()

    # Set up the mock driver's methods to return our mock elements
    mock_driver.return_value.find_element.side_effect = [mock_iframe, mock_save_button]

    # Create an instance of the class we're testing
    scraper = rainbowplantlife.RainbowPlantLifeScraper()

    # Set the driver attribute of the instance to the mock driver
    scraper.driver = mock_driver.return_value

    # Call the method we're testing
    scraper.accept_cookies()

    # Check that the methods were called with the correct arguments
    calls = [call(rainbowplantlife.By.CSS_SELECTOR, " #gdpr-consent-tool-wrapper > #gdpr-consent-notice"),
             call(rainbowplantlife.By.ID, "save")]
    mock_driver.return_value.find_element.assert_has_calls(calls)
    mock_driver.return_value.switch_to.frame.assert_called_once_with(mock_iframe)
    mock_save_button.click.assert_called_once()


@patch('selenium.webdriver.Chrome')
def test_close_ad(mock_driver):
    # Create a mock object for the ad element
    mock_ad = MagicMock()

    # Set up the mock driver's method to return our mock element
    mock_driver.return_value.find_element.return_value = mock_ad

    # Create an instance of the class we're testing
    scraper = rainbowplantlife.RainbowPlantLifeScraper()

    # Set the driver attribute of the instance to the mock driver
    scraper.driver = mock_driver.return_value

    # Call the method we're testing
    scraper.close_ad_bar()

    # Check that the method was called with the correct argument
    mock_driver.return_value.find_element.assert_called_once_with(rainbowplantlife.By.CLASS_NAME, "adthrive-close")
    mock_ad.click.assert_called_once()
