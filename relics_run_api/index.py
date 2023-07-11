import json
import gzip
import requests
from requests import Response
from typing import Any, Dict, Final

from .base import API_BASE_URL

API_INDEX_URL: Final[str] = API_BASE_URL + "/index/index.json.gz"


def get_index() -> Dict[str, Any]:
    """Get the index from the API.

    :return: The index from the API.
    :rtype: dict
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_index
        >>> get_index()
        {
            'relics': {
                'Axi A1': {
                    'Nikana Prime Blueprint': 3,
                    'Akstiletto Prime Barrel': 2,
                    'Dual Kamas Prime Handle': 2,
                    'Trinity Prime Systems Blueprint': 1,
                    'Fragor Prime Head': 1,
                    'Braton Prime Stock': 1
                }, ...
            },
            'non_vaulted': [
                'Axi G10',
                'Lith S15',
                'Neo S17',
                ...
            ],
            'prices': {
                'Frost Prime Set': 100.0,
                'Hydroid Prime Set': 104.5,
                'Zephyr Prime Chassis Blueprint': 5.5,
                ...
            },
            'ducats': {
                'Odonata Prime Blueprint': 45,
                'Odonata Prime Harness Blueprint': 15,
                'Odonata Prime Systems Blueprint': 15,
                ...
            },
            'required_count': {
                'Afuris Prime Barrel': 2,
                'Afuris Prime Receiver': 2,
                'Akbolto Prime Barrel': 2,
                ...
            },
            'types': {
                'Kavasa Prime': 'Skins',
                'Odonata Prime': 'Warframes',
                'Equinox Prime': 'Warframes',
                ...
            }
        }
    """

    # Get the index from the API
    response: Final[Response] = requests.get(API_INDEX_URL)

    # Check for errors
    response.raise_for_status()

    # Get the content of the response
    content: Final[str] = response.content

    # Decompress the content
    decompressed_content: Final[str] = gzip.decompress(content)

    # Parse the content
    parsed_content: Final[Dict[str, Any]] = json.loads(decompressed_content)

    # Return the parsed content
    return parsed_content
