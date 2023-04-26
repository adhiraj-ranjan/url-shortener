
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
    if 'url' in info:
        route.child(alias).update({"timestamp": int(time.time())})
        return info['url']
    else:
        return False


def perform_cleanup():
    data = route.get()
    if data:
        removed_lst = []
        current_stamp = int(time.time())
        for key in data.keys():
            if (current_stamp - route.child(key).get()['timestamp']) > 6015770000: # 6 months
                route.child(key).delete()
                removed_lst.append(key)
        return {"response": {"removed_aliases": removed_lst}}
    else:
        return {"response": "no data found"}
                