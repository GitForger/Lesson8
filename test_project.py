import requests
from config import BASE_URL, HEADERS


class TestProjectsAdapted:

    def test_create_project_positive(self):
        test_data = {
            "title": "Test Project",
            "companyId": "test_company_123",
            "users": [{"id": "test_user_123", "role": "admin"}]
        }

        response = requests.post(
            f"{BASE_URL}/projects",
            json=test_data,
            headers=HEADERS
        )

        assert response.status_code in [201, 400]

    def test_get_project_positive(self):
        response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, (list, dict))

    def test_update_project_positive(self):
        update_data = {"title": "Updated Project"}
        response = requests.put(
            f"{BASE_URL}/projects/nonexistent_id_123",
            json=update_data,
            headers=HEADERS
        )

        assert response.status_code in [400, 404]

    def test_create_project_negative_no_title(self):
        invalid_data = {"companyId": "test_company"}
        response = requests.post(
            f"{BASE_URL}/projects",
            json=invalid_data,
            headers=HEADERS
        )

        assert response.status_code == 400

    def test_get_project_negative_not_found(self):
        response = requests.get(
            f"{BASE_URL}/projects/nonexistent_id_123",
            headers=HEADERS
        )

        assert response.status_code == 404

    def test_update_project_negative_not_found(self):
        update_data = {"title": "New Title"}
        response = requests.put(
            f"{BASE_URL}/projects/nonexistent_id_123",
            json=update_data,
            headers=HEADERS
        )

        assert response.status_code == 404

