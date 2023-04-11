from firebase_admin import credentials
import firebase_admin
from app.api.trivia.controllers import get_most_similar_question_controller

def get_db():
    cred = credentials.Certificate("../secrets/nba-comparison-app-firebase-secret.json")

    db = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://nba-comparison-app-default-rtdb.firebaseio.com/'
    })
    return db

def test_get_most_similar_question_controller():
    """Test get most similar question controller"""
    player = {
        'name': 'LeBron James',
        'seasons': ['2023', '2022', '2021', '2020']
    }
    test_season = '2023'

    result = get_most_similar_question_controller(test_season, player)
    # print(result)

get_db()
test_get_most_similar_question_controller()