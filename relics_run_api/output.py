import requests
from typing import Dict, List, Final

from .base import API_BASE_URL

API_OUTPUT_URL: Final[str] = API_BASE_URL + "/output"
API_OUTPUT_TYPE_DICT_URL: Final[str] = API_OUTPUT_URL + "/type_dict.json"
API_OUTPUT_WFM_ITEMS_CATEGORIZED_URL: Final[str] = (
    API_OUTPUT_URL + "/wfm_items_categorized.json"
)


def get_output_type_dict() -> Dict[str, List[str]]:
    """Get the list of types from the API.

    :return: The list of types from the API.
    :rtype: Dict[str, List[str]]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_output_type_dict
        >>> get_output_type_dict()
        {
            "Relics": [
                "Lith K8 Relic",
                "Axi G10 Relic",
                "Lith H1 Relic",
                ...
            ],
            "Arcanes": [
                "Arcane Intention",
                "Arcane Phantasm",
                "Arcane Detoxifier",
                ...
            ],
            ...
        }
    """

    # Get the list of types from the API
    response: Final[Response] = requests.get(API_OUTPUT_TYPE_DICT_URL)

    # Check for errors
    response.raise_for_status()

    # Return the list of types
    return response.json()


def get_output_wfm_items_categorized() -> Dict[str, dict]:
    """Get the list of items from the API.

    :return: The list of items from the API.
    :rtype: Dict[str, dict]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_output_wfm_items_categorized
        >>> get_output_wfm_items_categorized()
        {
            "ArcaneHelmets": {
                "Arcane Aura Helmet": {
                    "item_name": "Arcane Aura Helmet",
                    "url_name": "arcane_aura_trinity_helmet",
                    "thumb": "items/images/en/thumbs/arcane_aura_trinity_helmet.d2b86ccdef9653830055ab389ef0d577.128x128.png",
                    "id": "54aaf1eee779890a8654131d"
                },
                ...
            },
            "Arcanes": {
                "Akimbo Slip Shot": {
                    "item_name": "Akimbo Slip Shot",
                    "url_name": "akimbo_slip_shot",
                    "thumb": "items/images/en/thumbs/akimbo_slip_shot.9cb48cdcc739b5306bb4e2a8b3868e72.128x128.png",
                    "id": "649322b07ec190215a693094"
                },
                ...
            },
            ...
        }
    """

    # Get the list of items from the API
    response: Final[Response] = requests.get(API_OUTPUT_WFM_ITEMS_CATEGORIZED_URL)

    # Check for errors
    response.raise_for_status()

    # Return the list of items
    return response.json()
