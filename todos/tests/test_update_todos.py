from todos.serializers import TodoCreateSerializer
from todos.db.services import TodosDBService
import pytest
from fastapi.testclient import TestClient

class TestUpdateTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos/'
        self.db_service = TodosDBService()
        todo = self.db_service.create_todo(TodoCreateSerializer(
            title='Todo1'
        ))
        self.id = todo.id

    def test_get_todos(self, client: TestClient):
        payload = dict(id=self.id, title='Todo2')
        response = client.put(self.url, json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == 'Todo2'
        todo = self.db_service.get_todo(self.id)
        assert todo.title == 'Todo2'
