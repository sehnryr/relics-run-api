import requests
from typing import Dict, List, Final

from .base import API_BASE_URL

API_MARKET_DATA_URL: Final[str] = API_BASE_URL + "/market_data"
API_MARKET_DATA_ITEMS_URL: Final[str] = API_MARKET_DATA_URL + "/items.json"


def get_market_data_items() -> List[Dict[str, str]]:
    """Get the list of items for which there is data in the API.

    :return: The list of items for which there is data in the API.
    :rtype: List[Dict[str, str]]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_market_data_items
        >>> get_market_data_items()
        [
            {'name': 'Axi A1'},
            {'name': 'Axi A2'},
            {'name': 'Axi A3'},
            ...
        ]
    """

    # Get the list of items from the API
    response: Final[Response] = requests.get(API_MARKET_DATA_ITEMS_URL)

    # Check for errors
    response.raise_for_status()

    # Return the list of items
    return response.json()
