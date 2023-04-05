import firebase_admin
from firebase_admin import credentials
from flask import g


def get_db():
    cred = credentials.Certificate("secrets/nba-comparison-app-firebase-secret.json")

    g.db = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nba-comparison-app-default-rtdb.firebaseio.com/'
    })
    return g.db

def init_db():
    db = get_db()
    return db

