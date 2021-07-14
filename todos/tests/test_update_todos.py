from todos.serializers import TodoCreateSerializer
from todos.db.services import TodosDBService
import pytest
from fastapi.testclient import TestClient

class TestUpdateTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos/'
        self.db_service = TodosDBService()
        self.todo = self.db_service.create_todo(TodoCreateSerializer(
            title='Todo1',
            description='Descrição',
            status='DOING',
            due_date='15/07/2021',
            responsible='João'
        ))

    def test_get_todos(self, client: TestClient):
        payload = dict(
            title='Todo2',
            description='Descrição2',
            status='DONE',
            due_date='15/07/2022',
            responsible='João2'
        )
        response = client.put(f'{self.url}/{self.todo.id}', json=payload)
        assert response.status_code == 200

        response_json = response.json()
        assert response_json['id'] == self.todo.id
        assert response_json['title'] == 'Todo2'
        assert response_json['description'] == 'Descrição2'
        assert response_json['status'] == 'DONE'
        assert response_json['due_date'] == '15/07/2022'
        assert response_json['responsible'] == 'João2'

        todos = self.db_service.get_todos()
        assert len(todos) == 1

        todo = todos[0]
        assert todo.id == self.todo.id
        assert todo.title == 'Todo2'
        assert todo.description == 'Descrição2'
        assert todo.status == 'DONE'
        assert todo.due_date == '15/07/2022'
        assert todo.responsible == 'João2'
