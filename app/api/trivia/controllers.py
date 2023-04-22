from app.utils.stats_helper import get_most_similar_row, get_player_index
from app.firebase.data.helpers import get_data_from_firebase
import pandas as pd

def get_season_stats_as_df_from_db(season):
    data = get_data_from_firebase(f'/player_season_stats/{season}/per_game')
    df = pd.DataFrame(data.values())
    return df



def get_most_similar_question_controller(test_season, player):
    """Get cards controller"""
    _, test_season_stats_df = get_player_index(get_season_stats_as_df_from_db(test_season), player['name'])

    for season in player['seasons']:

        player_row, season_stats_df = get_player_index(get_season_stats_as_df_from_db(season), player['name'])
        if player_row is None:
            print(f'Player {player["name"]} not found in season {season}')
        # most_similar_cosine = get_most_similar_row(test_season_stats_df, player_row, similarity_function="cosine")
        most_similar_pearson = get_most_similar_row(test_season_stats_df, player_row, similarity_function="pearson")
        # most_similar_euclidean = get_most_similar_row(test_season_stats_df, player_row, similarity_function="euclidean")

        print(f'Player: {player["name"]}, Season: {season}, Test Season: {test_season}')
        # print(most_similar_cosine)
        print(most_similar_pearson)
        # print(most_similar_euclidean)
    # return {
    #     'most_similar_cosine': most_similar_cosine,
    #     # 'most_similar_euclidean': most_similar_euclidean,
    #     'most_similar_pearson': most_similar_pearson
    # }
    return 'success'
