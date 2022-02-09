import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate(
    "./reactflightsearch-firebase-adminsdk-7vz6q-b6c4423253.json"
)

default_app = firebase_admin.initialize_app(
    cred_obj, {"databaseURL": "https://reactflightsearch-default-rtdb.firebaseio.com/"}
)

print(db.reference("/").get()["notify"])
