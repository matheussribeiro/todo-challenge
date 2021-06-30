import os
from todos.serializers import TodoCreateSerializer
import pytest
from fastapi.testclient import TestClient
from todos.db.services import TodosDBService

class TestGetTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos/'
        TodosDBService().create_todo(TodoCreateSerializer(
            title='Todo1'
        ))
        TodosDBService().create_todo(TodoCreateSerializer(
            title='Todo2'
        ))

    def test_get_todos(self, client: TestClient):
        response = client.get(self.url)
        assert response.status_code == 200
        response_json = response.json()
        assert len(response_json) == 2
        for todo in response_json:
            assert todo.get('title') in ['Todo1', 'Todo2']
