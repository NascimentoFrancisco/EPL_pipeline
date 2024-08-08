from typing import List, Dict


class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        """Simulates collecting name and link in an html
        - parameters:
            * html(str): html of a specific page to collect names and links
        - return:
            * A list of dictionaries with the collected names and links, like this:

            [
                {
                    'name': Name of the individual,
                    'link': Link linked to the individual
                },
                {
                    'name': Name of the individual,
                    'link': Link linked to the individual
                },
            ]
        """
        self.collect_essential_information_attributes["html"] = html
        return [{
            "name": "Algum nome",
            "link": "https://python.org"
        }]
