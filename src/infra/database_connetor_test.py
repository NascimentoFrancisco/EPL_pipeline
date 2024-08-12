from .database_connetor import DatabaseConnector

def test_connet():
    """Test if the connection to the database is successful"""

    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None
