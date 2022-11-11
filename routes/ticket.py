from fastapi import APIRouter
from models.ticket import Ticket
from database.ticket import create_ticket, get_ticket, get_tickets, delete_ticket, update_ticket


route_ticket = APIRouter()


@route_ticket.post("/create", response_model=Ticket, status_code=201)
def create(ticket: Ticket):
    return create_ticket(ticket.dict())



@route_ticket.get("/get/{id}")
def get_by_id(id: str):
    return get_ticket(id)



@route_ticket.get("/all")
def get_all():
    return get_tickets()



@route_ticket.delete("/delete/{id}/{created_at}")
def delete(id: str, created_at: str):
    return delete_ticket(id, created_at)



@route_ticket.put("/update")
def update(ticket: Ticket):
    return update_ticket(ticket.dict())
