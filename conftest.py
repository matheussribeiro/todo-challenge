import pytest
from db.services import DBService
from fastapi.testclient import TestClient


@pytest.fixture(scope='function', autouse=True)
def db_setup():
    DBService.create_tables()
    yield None
    DBService.destroy_tables()


@pytest.fixture(scope='function')
def client():
    from app import app
    client = TestClient(app)
    return client
