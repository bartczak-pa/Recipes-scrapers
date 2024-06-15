from unittest.mock import MagicMock, patch
from recipes_scrapers import rainbowplantlife


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
