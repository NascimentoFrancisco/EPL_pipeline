from typing import List, Dict
from bs4 import BeautifulSoup

class HtmlCollector:

    @classmethod
    def collect_essential_information(cls, html: str) -> List[Dict[str, str]]:
        """Collect name and links from the provided html
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
        soup = BeautifulSoup(html, "html.parser")

        artist_name_list = soup.find(class_="BodyText")
        artist_name_list_items = artist_name_list.find_all("a")

        essention_information = []
        for artist_name in artist_name_list_items:
            names = artist_name.contents[0]
            links = "https://web.archive.org"+artist_name.get("href")
            essention_information.append({
                "name": names,
                "link": links
            })

        return essention_information
