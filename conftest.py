import pytest
import requests
from config import HEADERS, BASE_URL

@pytest.fixture
def api_headers():
    return HEADERS.copy()

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def test_project_data():
    return {
        "title": "Test Project",
        "companyId": "test_company_123",
        "users": [{"id": "test_user_123", "role": "admin"}]
    }
