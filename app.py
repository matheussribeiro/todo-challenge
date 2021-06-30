from mangum import Mangum
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db.services import DBService
from todos.views import todo_router


app = FastAPI(
    title='Todo Aplication',
)

@app.get('/')
def status():
    return dict(status='OK')

app.include_router(
    todo_router,
    prefix='/todos',
    tags=['todos']
)


@app.on_event("startup")
async def startup_event():
    DBService.create_tables()


@app.exception_handler(Exception)
async def handle_all_exceptions(request: Request, error: Exception):
    return JSONResponse(
        status_code=500,
        content=str(error),
    )

handler = Mangum(app)
