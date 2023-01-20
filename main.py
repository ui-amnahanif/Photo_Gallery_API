from fastapi import FastAPI
from models import *
from typing import List
import pyodbc


app = FastAPI()

# DB
constr = "DRIVER={SQL Server}; SERVER=DESKTOP-JTGU3TR\\SQLEXPRESS; DATABASE=PhotoGallery; UID=abc; PWD=1234"
conn = pyodbc.connect(constr)
cursor = conn.cursor()


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
