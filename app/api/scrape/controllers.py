from app.utils.scraper import get_season_stats_as_df
from firebase_admin import db
def scrape_data_controller():
    season_stats_df = get_season_stats_as_df('2023')
    ref = db.reference("/")
    ref = db.reference("/player_season_stats/2023/per_game")
    for index, row in season_stats_df.iterrows():
        ref.push(row.to_dict())

    return 'success'


