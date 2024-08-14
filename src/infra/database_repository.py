from typing import Dict
from src.infra.database_connetor import DatabaseConnector


class DatabaseRepository:
    """Responsible for implementing queries in the database"""

    @classmethod
    def insert_artist(cls, data: Dict) -> None:
        """Inserts artist information into the database
        - parameters:
            * data(dict): Dictionary with the information to be entered
        - return:
            * None
        """
        query = """
            INSERT INTO artists 
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        """
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()
