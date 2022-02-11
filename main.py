import firebase_admin
import time
from firebase_admin import db
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("accountSID")
auth_token = os.getenv("authToken")
print(account_sid)

cred_obj = firebase_admin.credentials.Certificate(
    "./reactflightsearch-firebase-adminsdk-7vz6q-b6c4423253.json"
)

default_app = firebase_admin.initialize_app(
    cred_obj, {"databaseURL": "https://reactflightsearch-default-rtdb.firebaseio.com/"}
)
while True:
    time.sleep(1)
    to_notify = db.reference("/").get()["notify"]
    for notification in to_notify:
        # print(to_notify[notification])
        airportFrom = to_notify[notification]["airportFrom"]
        airportTo = to_notify[notification]["airportTo"]
        dateFrom = to_notify[notification]["dateFrom"]
        dateTo = to_notify[notification]["dateTo"]
        maxPrice = to_notify[notification]["maxPrice"]
        phone = to_notify[notification]["phone"]
