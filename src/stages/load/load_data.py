from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.stages.contracts.trasnform_contract import TransformContract
from src.errors.load_error import LoadError


class LoadData:
    """Class responsible for reading data and passing it to the database
    - paramenters:
        * repository(DatabaseRepositoryInterface): An instance of a class that 
        implements DatabaseRepositoryInterface
    """

    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        """Reads the data and uses the repository to save it
        - paramenters:
            * transformed_data_contract(TransformContract): An instance of TransformContract 
            that contains the data to be saved
        - return:
            * None
        """

        try:
            load_content = transformed_data_contract.load_content

            for data in load_content:
                self.__repository.insert_artist(data)
        except Exception as exception:
            raise LoadError(str(exception)) from exception
