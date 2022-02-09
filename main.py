import firebase_admin
import time
from firebase_admin import db

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
        print(to_notify[notification])
