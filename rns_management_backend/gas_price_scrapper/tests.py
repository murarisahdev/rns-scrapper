from unittest.mock import MagicMock, call, patch

from django.conf import settings
from django.test import TestCase
from gas_price_scrapper.tasks import fetch_and_store_gas_price


class TestScrapeAndStoreGasPrice(TestCase):
    @patch('gas_price_scrapper.tasks.requests.get')
    @patch('gas_price_scrapper.tasks.GasPrice.objects.create')
    def test_scrape_and_store_gas_price(self, mock_create, mock_get):
        # Set up mock response
        mock_response = MagicMock()
        mock_response.text = '<div class="text-right"><a href="/gastracker"><span>123.45 USD</span></a></div>'
        mock_get.return_value = mock_response

        # Call the task
        fetch_and_store_gas_price()

        # Assert that the task performed the expected operations
        mock_get.assert_called_once_with(settings.SCRAPPING_WEBSITE_URL)
        mock_create.assert_called_once_with(price=123.45)

    # @patch('gas_price_scrapper.tasks.requests.get')
    # @patch('gas_price_scrapper.tasks.GasPrice.objects.create')
    # def test_no_gas_price_found(self, mock_create, mock_get):
    #     # Set up mock response with no gas price
    #     mock_response = MagicMock()
    #     mock_response.text = '<div class="text-right"><a href="/gastracker"></a></div>'
    #     mock_get.return_value = mock_response

    #     # Call the task
    #     fetch_and_store_gas_price()

    #     # Assert that GasPrice.objects.create is not called
    #     mock_create.assert_not_called()
