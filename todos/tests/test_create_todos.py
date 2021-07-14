import pytest
from todos.db.services import TodosDBService
from fastapi.testclient import TestClient

class TestCreateTodos:
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.url = '/todos/'
        self.db_service = TodosDBService()

    def test_get_todos(self, client: TestClient):
        payload = dict(
            title='Todo1',
            description='Descrição',
            status='DOING',
            due_date='15/07/2021',
            responsible='João'
        )

        response = client.post(self.url, json=payload)
        assert response.status_code == 201

        response_json = response.json()
        assert response_json['id'] is not None
        assert response_json['title'] == 'Todo1'
        assert response_json['description'] == 'Descrição'
        assert response_json['status'] == 'DOING'
        assert response_json['due_date'] == '15/07/2021'
        assert response_json['responsible'] == 'João'

        todos = self.db_service.get_todos()
        assert len(todos) == 1

        todo = todos[0]
        assert todo.id is not None
        assert todo.title == 'Todo1'
        assert todo.description == 'Descrição'
        assert todo.status == 'DOING'
        assert todo.due_date == '15/07/2021'
        assert todo.responsible == 'João'
