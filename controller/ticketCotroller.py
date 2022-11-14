from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from service.ticketService import TicketService

class TicketController:

    def __init__(self, service: TicketService):
        self.service = service
    

    def create_ticket(self, ticket: dict):
        try:
            return self.service.create_ticket(ticket)
        except ClientError as e:
            return JSONResponse(content=e.response["Error"], status_code=500)


    def get_ticket(self, id: str):
        try:
            return self.service.get_ticket_by_id(id)
        except ClientError as e:
            return JSONResponse(content=e.response["Error"], status_code=500)


    def get_tickets(self):
        try:
            return self.service.get_tickets()
        except ClientError as e:
            return JSONResponse(content=e.response["Error"], status_code=500)


    def delete_ticket(self, id: str, created_at: str):
        try:
            return self.service.delete_ticket(id, created_at)
        except ClientError as e:
            return JSONResponse(content=e.response["Error"], status_code=500)


    def update_ticket(self, id: str,  ticket: dict):
        try:
            return self.service.update_ticket(id, ticket)
        except ClientError as e:
            return JSONResponse(content=e.response["Error"], status_code=500)
