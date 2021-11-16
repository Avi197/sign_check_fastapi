import os
import traceback
from datetime import datetime
from glob import glob

from fastapi import APIRouter, FastAPI, File, Form, UploadFile

from fastapi import requests
import dconfig
import vnd_log
from api_utils.constants import OLD_TEMPLATE_CONFIG
from api_utils.file_utils import save_pdf_and_img_file_timestamp


router = APIRouter(
    prefix='/compare',
    tags=['compare'],
    dependencies='',
    responses={404: {'description': 'Not found'}},
)

DATA_DIR = dconfig.config_object.DATA_DIR


# @router.get('/')
# async def smt():
#     return


@router.post('/pdf_old')
async def upload_compare_pdf(pdf: str = Form(...), template: str = Form(...)):
    form = await requests.form()
    filename = form["upload_file"].filename
    contents = await form["upload_file"].read()
    url_file_pdf = pdf
    url_template_img = template



