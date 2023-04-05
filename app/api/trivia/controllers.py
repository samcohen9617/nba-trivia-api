from app.utils.stats_helper import get_most_similar_row, get_player_index
from app.firebase.data.helpers import get_data_from_firebase
import pandas as pd

def get_season_stats_as_df(season):
    data = get_data_from_firebase(f'/player_season_stats/{season}/per_game')
    df = pd.DataFrame(data.values())
    return df



def get_most_similar_question_controller(season, player):
    """Get cards controller"""
    season_stats_df = get_season_stats_as_df(season)
    print(season_stats_df)

    player_index = get_player_index(season_stats_df, player)
    most_similar_cosine = get_most_similar_row(season_stats_df, player_index, similarity_function="cosine")
    most_similar_pearson = get_most_similar_row(season_stats_df, player_index, similarity_function="pearson")
    most_similar_euclidean = get_most_similar_row(season_stats_df, player_index, similarity_function="euclidean")

    print(most_similar_cosine)
    print(most_similar_pearson)
    print(most_similar_euclidean)
    return {
        'most_similar_cosine': most_similar_cosine,
        # 'most_similar_euclidean': most_similar_euclidean,
        'most_similar_pearson': most_similar_pearson
    }
