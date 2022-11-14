from abc import ABC, abstractmethod

class Service(ABC):

    @abstractmethod
    def create_ticket(self, ticket: dict):
        pass

    @abstractmethod
    def get_ticket_by_id(self, id: str):
        pass

    @abstractmethod
    def get_tickets(self):
        pass

    @abstractmethod
    def delete_ticket(self, id: str, created_at: str):
        pass

    @abstractmethod
    def update_ticket(self, id:str, ticket: dict):
        pass


