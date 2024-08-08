from datetime import date
from src.drivers.interfaces import HttpRequesterInterface
from src.drivers.interfaces import HtmlCollectorInterface
from src.stages.contracts import ExtractContract
from src.errors.extract_error import ExtractError


class ExtractHtml:

    def __init__(
        self,
        http_requester: HttpRequesterInterface,
        html_collector: HtmlCollectorInterface
    ) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector


    def extrac(self) -> ExtractContract:
        """Extracts essential information from html through internal methods
        - parameters:
            * None
        - return:
            * A namedtuple-based ExtractContract framework:

            ExtractContract(
                raw_information_content= extracted data, 
                extraction_date=datetime.date()
            )
        """
        try:
            html_information = self.__http_requester.request_from_page()
            essential_iformation = self.__html_collector.collect_essential_information(html_information["html"])

            return ExtractContract(
                raw_information_content=essential_iformation,
                extraction_date=date.today()
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
