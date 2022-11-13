import requests
from fastapi import HTTPException
from database.db import dynamodb
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
        person_response = requests.post(url = PERSON_ENDPOINT, json= data, headers=headers)
        #print("person sortId: " , person_response.json()["sortId"])
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
        if response["Count"] > 0:
            return response["Items"]
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_tickets():
    try:
        response = table.scan(
            Limit=10,
            AttributesToGet=["id", "concert", "sector", "person", "date", "quantity", "created_at"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def delete_ticket(id: str, created_at: str):
    try:
        item = table.query(
            KeyConditionExpression=Key("id").eq(id)
        )
        if item["Count"] > 0:
            response = table.delete_item(
            Key={
                "id": id,
                "created_at": created_at
            }
            )
            return response
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def update_ticket(ticket: dict):
    try:
        response = table.update_item(
            Key={
                "id": ticket["id"],
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
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)
