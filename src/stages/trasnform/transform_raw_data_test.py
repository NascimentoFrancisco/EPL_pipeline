from src.stages.contracts.mocks.extract_contract import extract_contract_mock
from src.stages.contracts.trasnform_contract import TransformContract
from src.errors.trasnform_error import TransformError
from .transform_raw_data import TransformRawData


def test_transform():

    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(extract_contract_mock)

    assert isinstance(transformed_information, TransformContract)
    assert "first_name" in transformed_information.load_content[0]
    assert "second_name" in transformed_information.load_content[0]
    assert "surname" in transformed_information.load_content[0]
    assert "artist_id" in transformed_information.load_content[0]
    assert "link" in transformed_information.load_content[0]
    assert "extraction_date" in transformed_information.load_content[0]


def test_transform_error():

    transform_raw_data = TransformRawData()
    try:
        transform_raw_data.transform("Entrada errada")
    except Exception as exception:
        assert isinstance(exception, TransformError)
