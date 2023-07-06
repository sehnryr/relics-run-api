from datetime import date
import re
import requests
from requests import Response
from typing import Dict, Final, List, Union

from base import API_BASE_URL

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
