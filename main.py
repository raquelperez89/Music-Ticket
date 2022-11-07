from fastapi import FastAPI
from database.db import create_tables
from routes.ticket import route_ticket


app = FastAPI()

app.include_router(route_ticket, prefix="/api")

#create_tables()