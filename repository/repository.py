from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def create(self, ticket: dict):
        pass

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self,  id: str, created_at: str):
        pass

    @abstractmethod
    def update(self, id:str, ticket: dict):
        pass



