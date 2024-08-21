from src.stages.extract.extract_html import ExtractHtml
from src.stages.trasnform.transform_raw_data import TransformRawData
from src.stages.load.load_data import LoadData
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.infra.database_connetor import DatabaseConnector
from src.infra.database_repository import DatabaseRepository

class MainPipeline:
    """Class responsible for running the entire pipeline process of this project"""

    def __init__(self) -> None:
        self.__extract_html = ExtractHtml(HttpRequester(), HtmlCollector())
        self.__trasnform_raw_data = TransformRawData()
        self.__load_data = LoadData(DatabaseRepository())

    def run_pipelide(self) -> None:
        """Executes and uses the resources needed to start and run the application
        - parameters:
            * None
        - return:
            * None
        """
        DatabaseConnector.connect()
        extract_contract = self.__extract_html.extrac()
        transformed_data_contract = self.__trasnform_raw_data.transform(extract_contract)
        self.__load_data.load(transformed_data_contract)
