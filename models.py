from pydantic import BaseModel
from typing import Optional
import datetime


class Album(BaseModel):
    id: int
    title: str


class Person(BaseModel):
    id: int
    name: str


class Photo(BaseModel):
    id: int
    title: str
    event: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    path: str
    date_taken: datetime.date
    last_modified_date: datetime.date


class AlbumPhoto(BaseModel):
    aid: int
    pid: int


class PhotoPerson(BaseModel):
    pid: int
    personid: int
