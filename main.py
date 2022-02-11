import firebase_admin
import requests
import time
from firebase_admin import db
from twilio.rest import Client
from dotenv import load_dotenv
import os
import json

load_dotenv()


def dateConverter(date):
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    return f"{day}/{month}/{year}"


account_sid = os.getenv("accountSID")
auth_token = os.getenv("authToken")
kiwi_api_key = os.getenv("kiwiAPI")
client = Client(account_sid, auth_token)

cred_obj = firebase_admin.credentials.Certificate(
    "./reactflightsearch-firebase-adminsdk-7vz6q-b6c4423253.json"
)

default_app = firebase_admin.initialize_app(
    cred_obj, {"databaseURL": "https://reactflightsearch-default-rtdb.firebaseio.com/"}
)
while True:
    to_notify = db.reference("/").get()["notify"]
    for notification in to_notify:

        airportFrom = to_notify[notification]["airportFrom"]
        airportTo = to_notify[notification]["airportTo"]
        dateFrom = to_notify[notification]["dateFrom"]
        dateTo = to_notify[notification]["dateTo"]
        maxPrice = to_notify[notification]["maxPrice"]
        phone = to_notify[notification]["phone"]

        # Converting dates in place
        dateFrom = dateConverter(dateFrom)
        dateTo = dateConverter(dateTo)
        flight_info = requests.get(
            url="http://tequila-api.kiwi.com/v2/search",
            params={
                "fly_from": airportFrom,
                "date_from": dateFrom,
                "date_to": dateTo,
                "fly_to": airportTo,
                "one_for_city": "1",
                "curr": "USD",
            },
            headers={"apikey": kiwi_api_key},
        )
        fljs = json.loads(flight_info.text)
        current_price = fljs["data"][0]["price"]
        if current_price <= maxPrice:
            print("hit")
            message = client.messages.create(
                body=fljs["data"][0],
                from_="+18312222233",
                to="+18138416890",
            )
        time.sleep(10000)
