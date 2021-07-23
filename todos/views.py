from pynamodb.attributes import NullAttribute
from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from typing import List
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, PlainTextResponse
from .serializers import TodoSerializer, TodoCreateSerializer, TodoUpdateSerializer

todo_router = APIRouter()


@todo_router.get('/')
async def get_todo():
    return TodosDBService().get_todos()


@todo_router.post('/',status_code=201)
async def create_todo(todo: TodoCreateSerializer):
    return TodosDBService().create_todo(todo)


@todo_router.get('/{id}')
async def get_one_todo(id: str):
    return TodosDBService().get_todo(id)

@todo_router.put('/{id}')
async def update_todo(id: str , todo : TodoUpdateSerializer):
    return TodosDBService().update_todo(id,todo)


@todo_router.delete('/{id}')
async def delete_todo(id: str):
    return TodosDBService().delete_todo(id)









'''
GET todos/
'''

''''
GET todos/{id}/
'''

'''
POST todos
'''

'''
PUT todos
'''

''''
DELETE todos/{id}/
'''
