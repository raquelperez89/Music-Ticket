from fastapi import APIRouter
from models.ticket import Ticket
from controller.ticketController import TicketController
from service.ticketService import TicketService
from repository.ticketRepository import TicketRepository


route_ticket = APIRouter()

ticketRepository = TicketRepository()
ticketService = TicketService(ticketRepository)
ticketController = TicketController(ticketService)

@route_ticket.post("/tickets", response_model=Ticket, status_code=201)
def create(ticket: Ticket):
    return ticketController.create_ticket(ticket.dict())



@route_ticket.get("/tickets/{id}")
def get_by_id(id: str):
    return ticketController.get_ticket(id)



@route_ticket.get("/tickets")
async def get_all():
    return ticketController.get_tickets()



@route_ticket.delete("/tickets/{id}/{created_at}")
def delete(id: str, created_at: str):
    return ticketController.delete_ticket(id, created_at)



@route_ticket.put("/tickets/{id}")
def update(id:str, ticket: Ticket):
    return ticketController.update_ticket(id, ticket.dict())
