import firebase_admin
from firebase_admin import credentials, db
from app.utils.scraper import get_season_stats_as_df

def get_db():
    cred = credentials.Certificate("../secrets/nba-comparison-app-firebase-secret.json")

    db = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nba-comparison-app-default-rtdb.firebaseio.com/'
    })
    return db

def scrape_seasons(seasons):
    for season in seasons:
        season_stats_df = get_season_stats_as_df(season)
        ref = db.reference("/player_season_stats/" + season + "/per_game")
        for index, row in season_stats_df.iterrows():
            ref.push(row.to_dict())
get_db()
scrape_seasons(['2023', '2022', '2021', '2020'])
