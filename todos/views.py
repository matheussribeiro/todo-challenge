from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from typing import List
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, PlainTextResponse
from .serializers import TodoSerializer, TodoCreateSerializer

todo_router = APIRouter()


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
