from datetime import date
import re
import requests
from requests import Response
from typing import Dict, Final, List, Union

from .base import API_BASE_URL

API_HISTORY_URL: Final[str] = API_BASE_URL + "/history"
API_HISTORY_DATE_URL: Final[str] = API_HISTORY_URL + "/price_history_{date}.json"


def get_history_dates() -> List[date]:
    """Get the list of dates for which there is data in the API.

    :return: The list of dates for which there is data in the API.
    :rtype: List[date]
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from relics_run_api import get_history_dates
        >>> get_history_dates()
        [datetime.date(2023, 7, 2), datetime.date(2023, 7, 3), datetime.date(2023, 7, 4)]
    """

    # Get the list of dates from the API
    response: Final[Response] = requests.get(API_HISTORY_URL)

    # Check for errors
    response.raise_for_status()

    # Get the content of the response
    content: Final[str] = response.text

    # Create the regex to match the dates
    date_regex = re.compile(r'href="price_history_(\d{4}-\d{2}-\d{2})\.json"')

    # Find all the dates
    dates: List[str] = date_regex.findall(content)

    # Convert the dates to date objects
    dates = [date.fromisoformat(date_string) for date_string in dates]

    # Sort the dates in ascending order
    dates.sort()

    # Return the dates
    return dates


def get_history(date: date) -> Dict[str, List[Dict[str, Union[str, int, float]]]]:
    """Get the data for a given date from the API.

    :param date: The date for which to get the data.
    :type date: date
    :return: The data for the given date.
    :rtype: dict
    :raises requests.HTTPError: If there is an error with the request.

    Usage::

        >>> from datetime import date
        >>> from relics_run_api import get_history
        >>> get_history(date=date(2023, 7, 2))
        {
            'Secura Dual Cestra': [
                {
                    'datetime': '2023-07-02T00:00:00.000+00:00',
                    'volume': 8,
                    'min_price': 25,
                    'max_price': 40,
                    'open_price': 30,
                    'closed_price': 34,
                    'avg_price': 32.5,
                    'wa_price': 32.375,
                    'median': 30.0,
                    'moving_avg': 30.2,
                    'donch_top': 40,
                    'donch_bot': 20,
                    'id': '64a20ff4ca73520023c44a7f'
                }, {
                    'datetime': '2023-07-02T00:00:00.000+00:00',
                    'volume': 435,
                    'min_price': 10,
                    'max_price': 15,
                    'avg_price': 12.5,
                    'wa_price': 10.062,
                    'median': 13,
                    'order_type':
                    'buy',
                    'moving_avg': 21.6,
                    'id': '64a20ff4ca73520023c44a81'
                }, {
                    'datetime': '2023-07-02T00:00:00.000+00:00',
                    'volume': 117,
                    'min_price': 20,
                    'max_price': 45,
                    'avg_price': 32.5,
                    'wa_price': 32.846,
                    'median': 30,
                    'order_type': 'sell',
                    'moving_avg': 25.3,
                    'id': '64a20ff4ca73520023c44a80'
                }
            ],
            [...]
        }
    """

    # Build the URL
    url: Final[str] = API_HISTORY_DATE_URL.format(date=date.isoformat())

    # Get the data from the API
    response: Final[Response] = requests.get(url)

    # Check for errors
    response.raise_for_status()

    # Return the data
    return response.json()
