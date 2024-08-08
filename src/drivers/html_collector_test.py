from .html_collector import HtmlCollector
from .mocks import mock_request_from_page

def test_collect_essential_information():
    http_request_response = mock_request_from_page()

    html_collector = HtmlCollector()
    essention_information = html_collector.collect_essential_information(http_request_response["html"])

    assert isinstance(essention_information, list)
    assert isinstance(essention_information[0], dict)
    assert "name" in essention_information[0]
    assert "link" in essention_information[0]
