# conftest.py
import pytest
from unittest.mock import Mock
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', filename='../../logs/test.log', filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

setup_logging()

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_auth_token"
    }

@pytest.fixture
def post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

@pytest.fixture
def mock_response():
    def _mock_response(status_code=200, json_data=None):
        mock = Mock()
        mock.status_code = status_code
        mock.json = Mock(return_value=json_data)
        return mock
    return _mock_response
