from app.utils.scraper import get_random_player, get_random_active_player, get_season_stats_as_df
from app.utils.stats_helper import get_most_similar_row_cosine, get_most_similar_row_euclidean, get_player_index, get_most_similar_row_pearsonian
def get_nickname_question_controller():
    """Get cards controller"""
    player = get_random_active_player()
    return player


def get_most_similar_question_controller(season, player):
    """Get cards controller"""
    season_stats_df = get_season_stats_as_df(season)
    player_index = get_player_index(season_stats_df, player)
    most_similar_cosine = get_most_similar_row_cosine(season_stats_df, player_index)
    # most_similar_euclidean = get_most_similar_row_euclidean(season_stats_df, player_index)
    # most_similar_pearson = get_most_similar_row_pearsonian(season_stats_df, player_index)

    return {
        'most_similar_cosine': most_similar_cosine,
        # 'most_similar_euclidean': most_similar_euclidean,
        # 'most_similar_pearson': most_similar_pearson
    }
