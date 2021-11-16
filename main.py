import os.path
import random
import uvicorn
from typing import Optional
from fastapi import FastAPI, APIRouter
from fastapi.responses import PlainTextResponse


def create_app():
    app = FastAPI()
    # router = APIRouter()
    try:
        if not os.path.exists('log'):
            os.makedirs('log')
    except OSError:
        pass

    @app.get('/', response_class=PlainTextResponse)
    def home():
        return 'go to ... to upload file'

    return app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, host='')





# from typing import Optional
#
# from fastapi import FastAPI, Form, UploadFile, File
# from starlette.requests import Request
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.post("/login/")
# async def login(file: UploadFile = File(...), password: str = Form(...), abc: str = Form(...)):
#     return {"username": password, 'abc': abc, }
#
#
# @app.post("/request-passing")
# async def request_passing(request: Request) -> dict:
#     return {"choices": (await request.form()).getlist("choices")}
#
#
# @app.post('/test/')
# async def upload_test(file: UploadFile = File(...), file2: UploadFile = File(...)):
#     return {
#         'file': file,
#         'file1': file2,
#     }
#
#
# @app.post("/upload/")
# async def upload(fileb: UploadFile = File(...)):
#     return {
#         "fileb_content_type": fileb.content_type,
#     }
