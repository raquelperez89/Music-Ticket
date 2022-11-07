import requests
from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("tickets")
PERSON_ENDPOINT = "https://ad-band-service.herokuapp.com/api/Person"
headers={
    'Content-type':'application/json', 
    'Accept':'*/*'
}

def create_ticket(ticket: dict):
    try:
        data = ticket["person"]
        person_response = requests.post(url = PERSON_ENDPOINT, data = data, headers=headers)
        print(ticket["person"])
        #print(r.status_code)
        # ticket["person.name"] = "nothing"
        if person_response.status_code == 200:
            table.put_item(Item=ticket)
            return ticket
        else :
            return JSONResponse(content="Person not valid", status_code=person_response.status_code)
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_ticket(id: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("id").eq(id)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_tickets():
    try:
        response = table.scan(
            Limit=5,
            AttributesToGet=["id", "concert", "sector", "person", "date", "quantity"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_ticket(ticket: dict):
    try:
        response = table.delete_item(
            Key={
                "id": ticket["id"],
                "created_at": ticket["created_at"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_ticket(ticket: dict):
    try:
        response = table.update_item(
            Key={
                "id": ticket["id"],
                "created_at": ticket["created_at"]
            },
            UpdateExpression="SET #quantity = :quantity, #date = :date",
            ExpressionAttributeValues={
                ":quantity": ticket["quantity"],
                ":date": ticket["date"]
            },
            ExpressionAttributeNames={
                "#quantity": "quantity",
                "#date": "date"
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
