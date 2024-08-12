import mysql.connector as mysql

class DatabaseConnector:
    """Class responsible for connecting to the database"""

    connection = None

    @classmethod
    def connect(cls) -> None:
        """Changes the database connection state
        - parameters:
            * None
        - return:
            * None
        """
        db_coonection = mysql.connect(
            host="localhost",
            port="3306",
            database="pipeline_db",
            user="root",
            passwd="root"
        )
        cls.connection = db_coonection
