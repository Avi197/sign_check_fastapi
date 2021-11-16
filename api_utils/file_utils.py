import os
import shutil
from datetime import datetime

import dconfig
import vnd_log

DATA_DIR = dconfig.config_object.DATA_DIR


def create_empty_dir(pathname):
    if os.path.isdir(pathname):
        for filename in os.listdir(pathname):
            file_path = os.path.join(pathname, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                vnd_log.dlog_e('Failed to delete {}. Reason: {}'.format(file_path, e))
    else:
        os.makedirs(pathname)


def save_pdf_file_timestamp(url_file):
    now = datetime.now()
    timestamp_name = now.strftime("%Y%m%d%H%M%S%f")
    pdf_path = os.path.join(DATA_DIR, 'temp', f'{timestamp_name}.pdf')
    url_file.save(pdf_path)
    return pdf_path


def save_pdf_and_img_file_timestamp(url_file_pdf, url_template_img):
    now = datetime.now()
    timestamp_name = now.strftime("%Y%m%d%H%M%S%f")
    pdf_path = os.path.join(DATA_DIR, 'temp', f'{timestamp_name}.pdf')
    url_file_pdf.save(pdf_path)

    image_suffix = url_template_img.filename[url_template_img.filename.rfind('.'):]
    img_path = os.path.join(DATA_DIR, 'temp', f'{timestamp_name}{image_suffix}')
    url_template_img.save(img_path)
    return pdf_path, img_path
