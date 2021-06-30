import pytest
from fastapi.testclient import TestClient

class TestCreateTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos/'

    def test_get_todos(self, client: TestClient):
        payload = dict(title='Todo1')
        response = client.post(self.url, json=payload)
        assert response.status_code == 201
        response_json = response.json()
        assert response_json['title'] == 'Todo1'
