from database.db import dynamodb
from boto3.dynamodb.conditions import Key

from repository.repository import Repository

table = dynamodb.Table("tickets")


class TicketRepository(Repository):

    def create(self, ticket: dict):
        table.put_item(Item=ticket)
        return ticket
    

    def get_by_id(self, id: str):
        response = table.query(
            KeyConditionExpression=Key("id").eq(id)
        )
        return response


    def get_all(self):
        response = table.scan(
            Limit=5,
            AttributesToGet=["id", "concert", "sector", "person", "date", "quantity", "created_at"]
        )
        return response["Items"]
    

    def delete(self, id: str, created_at: str):
        response = table.delete_item(
        Key={
            "id": id,
            "created_at": created_at
        }
        )
        return response


    def update(self, id:str, ticket: dict):
        response = table.update_item(
            Key={
                "id": id,
                "created_at": ticket["created_at"]
            },
            UpdateExpression="SET #quantity = :quantity, #date = :date, #sector = :sector",
            ExpressionAttributeValues={
                ":quantity": ticket["quantity"],
                ":date": ticket["date"],
                ":sector": ticket["sector"]
            },
            ExpressionAttributeNames={
                "#quantity": "quantity",
                "#date": "date",
                "#sector": "sector"
            }
        )
        return response

