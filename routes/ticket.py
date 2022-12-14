from fastapi import APIRouter
from models.ticket import Ticket
from database.ticket import create_ticket, get_ticket, get_tickets, delete_ticket, update_ticket


route_ticket = APIRouter()


@route_ticket.post("/create", response_model=Ticket)
def create(ticket: Ticket):
    return create_ticket(ticket.dict())



@route_ticket.get("/get/{id}")
def get_by_id(id: str):
    return get_ticket(id)



@route_ticket.get("/all")
def get_all():
    return get_tickets()



@route_ticket.post("/delete")
def create(ticket: Ticket):
    return delete_ticket(ticket.dict())



@route_ticket.put("/update")
def create(ticket: Ticket):
    return update_ticket(ticket.dict())
