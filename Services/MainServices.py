import os
import shutil
from os.path import dirname, join, realpath

UPLOAD_FOLDERL = join(dirname(realpath(__file__)), 'static/croppedL/')


def clean_dir():
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/images')
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/croppedW')
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/croppedL/0')
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/croppedL/1')
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/croppedL/2')
    shutil.rmtree('/home/msbomrel/PycharmProjects/cheque/static/croppedL/3')

    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/images')
    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/croppedW')
    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/croppedL/0')
    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/croppedL/1')
    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/croppedL/2')
    os.mkdir('/home/msbomrel/PycharmProjects/cheque/static/croppedL/3')


# def clean_croppedletters():
#     os.execute(UPLOAD_FOLDERL +'find . -name \*.png -type f -delete')