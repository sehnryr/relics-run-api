import requests
from typing import Dict, List, Final

from .base import API_BASE_URL

API_MARKET_DATA_URL: Final[str] = API_BASE_URL + "/market_data"
API_MARKET_DATA_ITEM_IDS_URL: Final[str] = API_MARKET_DATA_URL + "/item_ids.json"
API_MARKET_DATA_ITEM_INFO_URL: Final[str] = API_MARKET_DATA_URL + "/item_info.json"
API_MARKET_DATA_ITEMS_URL: Final[str] = API_MARKET_DATA_URL + "/items.json"


def get_market_data_item_ids() -> Dict[str, str]:
    """Get the list of item IDs for which there is data.

    :return: The list of item IDs for which there is data.
    :rtype: Dict[str, str]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_market_data_item_ids
        >>> get_market_data_item_ids()
        {
            "Secura Dual Cestra": "54aae292e7798909064f1575",
            "Creeping Bullseye": "54ca39abe7798915c1c11e10",
            "Mutalist Alad V Assassinate (Key)": "54d4c727e77989281cc7d753",
            ...
        }
    """
    # Get the list of item IDs from the API
    response: Final[Response] = requests.get(API_MARKET_DATA_ITEM_IDS_URL)

    # Check for errors
    response.raise_for_status()

    # Return the list of item IDs
    return response.json()


def get_market_data_item_info() -> Dict[str, dict]:
    """Get the list of item info for which there is data.

    :return: The list of item info for which there is data.
    :rtype: Dict[str, dict]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_market_data_item_info
        >>> get_market_data_item_info()
        {
            "54aae292e7798909064f1575": {
                "set_items": [],
                "item_id": "54aae292e7798909064f1575",
                "tags": [
                    "syndicate",
                    "weapon",
                    "secondary"
                ],
                "mod_max_rank": null,
                "subtypes": []
            },
            ...
        }
    """
    # Get the list of item info from the API
    response: Final[Response] = requests.get(API_MARKET_DATA_ITEM_INFO_URL)

    # Check for errors
    response.raise_for_status()

    # Return the list of item info
    return response.json()


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
