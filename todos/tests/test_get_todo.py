from todos.serializers import TodoCreateSerializer
import pytest
from fastapi.testclient import TestClient
from todos.db.services import TodosDBService

class TestGetTodo:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos'
        self.todo = TodosDBService().create_todo(TodoCreateSerializer(
            title='Todo1'
        ))

    def test_get_todos(self, client: TestClient):
        response = client.get(f'{self.url}/{self.todo.id}/')
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == 'Todo1'
