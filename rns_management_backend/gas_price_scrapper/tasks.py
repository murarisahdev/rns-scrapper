import logging
import re

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.conf import settings

from .models import GasPrice

logger = logging.getLogger(__name__)

@shared_task
def fetch_and_store_gas_price():
    """
    Task to fetch the current gas price from a website and store it in the database.
    """
    try:
        # Get the gas price from the specified website URL
        logger.info('Fetching gas price...')
        response = requests.get(settings.SCRAPPING_WEBSITE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        price = None

        # Extract the gas price from the HTML content
        div = soup.find('div', class_='text-right')
        if div:
            span_tag = div.find('span', class_='new-line-xxs')
            if span_tag:
                span_tag = div.find('span', class_='small break-all text-slate-500 ml-1')
                if span_tag:
                    span_text = span_tag.text.strip()  # Remove leading/trailing whitespace
                    # Use regular expression to extract the numerical part
                    price_text = re.search(r'\d+\.\d+', span_text)
                    if price_text:
                        price = float(price_text.group())
                    else:
                        logger.warning('No valid gas price found in span text.')
                else:
                    logger.warning('No gas price text found in span tag.')
            else:
                logger.warning('No span tag found for gas price.')
        else:
            logger.warning('No div with class "text-right" found in HTML content.')

        # Store the gas price in the database if it's valid
        if price is not None:
            GasPrice.objects.create(price=price)
            logger.info('Gas price fetched and stored successfully.')
    except Exception as e:
        logger.error(f'An error occurred while fetching and storing gas price: {str(e)}')
