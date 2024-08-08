from typing import Dict

class HttpRequesterSpy:

    def __init__(self) -> None:
        self.request_from_page_count = 0

    def request_from_page(self) -> Dict[int, str]:
        """Method adapted for testing, this simulates a request in a url and returns a dictionary with the request data
        - parameters:
            * None
        - return:
            * Dictionary with the result of the GET request with:

            {
                "status_code": integer value of the status code, 
                "html": html of the page
            }
        """
        self.request_from_page_count += 1
        return {
            "status_code": 200,
            "html": "</h1>HTML para testes</>"
        }
