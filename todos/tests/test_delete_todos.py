from todos.serializers import TodoCreateSerializer
from todos.db.services import TodosDBService
import pytest
from fastapi.testclient import TestClient

class TestDeleteTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos'
        self.db_service = TodosDBService()
        todo = self.db_service.create_todo(TodoCreateSerializer(
            title='Todo1'
        ))
        self.id = todo.id

    def test_get_todos(self, client: TestClient):
        assert len(self.db_service.get_todos()) == 1
        response = client.delete(f'{self.url}/{self.id}/')
        assert response.status_code == 204
        assert len(self.db_service.get_todos()) == 0
