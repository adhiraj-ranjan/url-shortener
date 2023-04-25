
import firebase_admin
from firebase_admin import credentials, db
import time
from base64 import b64decode
from json import loads
from os import environ

CREDS = loads(b64decode(environ['token']).decode())

cred = credentials.Certificate(CREDS)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://urlshortener-records-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

route = db.reference("routes/")

def create_route(alias, url):
    if not route.child(alias).get():
        route.update({alias: {"url": url, "timestamp": int(time.time())}})
        return True
    else:
        return False

def get_redirection_url(alias):
    info = route.child(alias).get()
    if info:
        route.child(alias).update({"timestamp": int(time.time())})
        return info['url']
    else:
        return False
