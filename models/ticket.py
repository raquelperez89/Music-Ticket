from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime, date


def generate_id():
    return str(uuid4())


def generate_date():
    return str(datetime.now())


class Concert(BaseModel):
    location: str
    date: str
    stadium: str


class Sector(BaseModel):
    name: str
    price: int


class Person(BaseModel):
    name: str
    email: str
    dateOfBirth: str
    nationality: str


class Ticket(BaseModel):
    id: str = Field(default_factory=generate_id)
    concert:  Concert
    sector: Sector
    person: Person
    date: str
    quantity: int
    created_at: str = Field(default_factory=generate_date)


