import requests
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from repository.ticketRepository import TicketRepository

PERSON_ENDPOINT = "https://ad-band-service.herokuapp.com/api/Person"
headers={
    'Content-type':'application/json', 
    'Accept':'*/*'
}

class TicketService:


    def __init__(self, repository: TicketRepository):
        self.repository = repository

    def create_ticket(self, ticket: dict):
        data = ticket["person"]
        person_response = requests.post(url = PERSON_ENDPOINT, json= data, headers=headers)
        #print("person sortId: " , person_response.json()["sortId"])
        if person_response.status_code == 200:
            self.repository.create(ticket)
            return ticket
        else :
            return JSONResponse(content="Person not valid", status_code=person_response.status_code)


    def get_ticket_by_id(self, id: str):
        response = self.repository.get_by_id(id)
        if response["Count"] > 0:
            return response["Items"]
        else:
            raise HTTPException(status_code=404, detail="Item not found")


    def get_tickets(self):
        return self.repository.get_all()

    def delete_ticket(self, id: str, created_at: str):
        item = self.repository.get_by_id(id)
        if item["Count"] > 0:
            response = self.repository.delete(id, created_at)
            return response
        else:
            raise HTTPException(status_code=404, detail="Item not found")

    def update_ticket(self, id:str, ticket: dict):
        item = self.repository.get_by_id(id)
        if item["Count"] > 0:
            response = self.repository.update(id, ticket)
            return response
        else:
            raise HTTPException(status_code=404, detail="Item not found")
