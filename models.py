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
    id: Optional[int]
    title: str
    event: Optional[str]
    lat: Optional[float]
    lng: Optional[float]
    path: Optional[str]
    date_taken: datetime.datetime
    last_modified_date: datetime.datetime


class AlbumPhoto(BaseModel):
    aid: int
    pid: int


class PhotoPerson(BaseModel):
    pid: int
    personid: int
