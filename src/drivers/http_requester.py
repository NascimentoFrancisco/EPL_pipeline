from typing import Dict
import requests
from src.drivers.interfaces import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):
    """Class responsible for making the request in the URL in which the data is present"""

    def __init__(self) -> None:
        self.__url = "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"

    def request_from_page(self) -> Dict[int, str]:
        """Gets information from a page, returning a dictionary with the result of the GET request
        - parameters:
            * None
        - return:
            * Dictionary with the result of the GET request with:

            {
                "status_code": integer value of the status code, 
                "html": html of the page
            }
        """
        response = requests.get(self.__url, timeout=10)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
