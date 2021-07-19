from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from typing import List
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, PlainTextResponse
from .serializers import TodoSerializer, TodoCreateSerializer

todo_router = APIRouter()

@todo_router.get('/')
async def get_todo():
    return dict(message = 'GetFunfouTuéBrabo')


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
