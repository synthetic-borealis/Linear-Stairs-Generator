#!python
import os
from posixpath import basename
import shutil
from os import path
from zipfile import ZipFile

OUTPUT_NAME = "LinearStairsGenerator"
VERSION_STRING = "v0.0.2"
OUTPUT_FILE_NAME = "{0}_{1}.zip".format(OUTPUT_NAME, VERSION_STRING)

def copytree_to_outdir(src):
    shutil.copytree(src, path.join(OUTPUT_NAME, src))


def copy_to_outdir(src):
    shutil.copy(src, path.join(OUTPUT_NAME, src))

if (path.exists(OUTPUT_NAME)):
    if path.isdir(OUTPUT_NAME):
        shutil.rmtree(OUTPUT_NAME)
    else:
        os.remove(OUTPUT_NAME)

if (path.exists(OUTPUT_FILE_NAME)):
    if path.isdir(OUTPUT_FILE_NAME):
        shutil.rmtree(OUTPUT_FILE_NAME)
    else:
        os.remove(OUTPUT_FILE_NAME)

os.mkdir(OUTPUT_NAME)

copytree_to_outdir("operators")
copytree_to_outdir("utils")
copy_to_outdir("__init__.py")

with ZipFile(OUTPUT_FILE_NAME, "w") as out_file:
    for folder_name, subfolder, filenames in os.walk(OUTPUT_NAME):
        for filename in filenames:
            file_path = path.join(folder_name, filename)
            out_file.write(file_path, basename(file_path))

shutil.rmtree(OUTPUT_NAME)
