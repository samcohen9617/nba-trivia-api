import firebase_admin
from firebase_admin import credentials, db
from app.utils.scraper import get_season_stats_as_df

def get_db():
    cred = credentials.Certificate("../secrets/nba-comparison-app-firebase-secret.json")

    db = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nba-comparison-app-default-rtdb.firebaseio.com/'
    })
    return db

get_db()

def delete_seasons(seasons):
    for season in seasons:
        ref = db.reference("/player_season_stats/" + season)
        ref.delete()
        print(f'Deleted season {season}')
delete_seasons([ '2023', '2022', '2021', '2020'])