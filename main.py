import os
import shutil
from fastapi import FastAPI, UploadFile, File, Query, Path, Form, Depends
from models import *
from typing import List
from pydantic import Required
import pyodbc


app = FastAPI()

# DB
constr = "DRIVER={SQL Server}; SERVER=DESKTOP-JTGU3TR\\SQLEXPRESS; DATABASE=PhotoGallery; UID=abc; PWD=1234"
conn = pyodbc.connect(constr)
cursor = conn.cursor()

# Utilities
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Utitlity Function


def Allowed_File(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get('/')
def index():
    return "Hello"


@app.get('/getAllAlbums')
def getAllAlbums():
    query = "SELECT * FROM Album"
    cursor.execute(query)
    data = cursor.fetchall()
    albums: List[Album] = []
    for row in data:
        item = Album(id=row.id, title=row.title)
        albums.append(item)
    return albums


@app.get('/getAllPhotos')
def getAllPhotos():
    query = "SELECT * FROM Photo"
    cursor.execute(query)
    data = cursor.fetchall()
    photos: List[Photo] = []
    for row in data:
        item = Photo(id=row.id, title=row.title, event=row.event, lat=row.lat, lng=row.lng,
                     path=row.path, date_taken=row.date_taken, last_modified_date=row.last_modified_date)
        photos.append(item)
    return photos


@app.post('/uploadPhoto')
def uploadPhoto(file: UploadFile, photoDetail: Photo = Depends()):
    filePath = f"Images/{file.filename}"

    if Allowed_File(file.filename):
        fp = open(filePath, 'w')
        fp.close()
        with open(filePath, 'wb+') as buffer:
            shutil.copyfileobj(file.file, buffer)

    query = "INSERT INTO Photo(title, event, lat, lng, path, date_taken, last_modified_date) VALUES (?,?,?,?,?,?,?)"

    cursor.execute(query,
                   photoDetail.title,
                   photoDetail.event,
                   photoDetail.lat,
                   photoDetail.lng,
                   filePath,
                   photoDetail.date_taken,
                   photoDetail.last_modified_date)
    cursor.commit()
    return "File Uploaded Successfully"
