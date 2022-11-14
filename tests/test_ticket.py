import unittest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from service.ticketService import TicketService


class ServiceTest(unittest.TestCase):
    def setUp(self):
        self.repositoryMock = Mock()
        self.repositoryMock.get_all()
        self.service = TicketService(self.repositoryMock)
        

    def test_get_tickets(self):
        self.service.get_tickets()
        print(self.service.get_tickets())
        self.assertEqual(self.repositoryMock().get_all.call_count, 1)




