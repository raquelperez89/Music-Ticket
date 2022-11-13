from fastapi import FastAPI
from database.db import create_tables
from routes.ticket import route_ticket

app = FastAPI(title="Music Tickets")

app.include_router(route_ticket, prefix="/api", tags=["Tickets"])

#create_tables()