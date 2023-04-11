from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler
import heapq

EXCLUDED_COLUMNS = ['Player', 'Age', 'Rk', 'Tm', 'G', 'GS', 'Pos']


def get_player_index(df, player_name):
    # Get all rows where the player name is the same
    player_rows = df.loc[df["Player"] == player_name]
    if len(player_rows) == 0:
        return None, df


    #drop the rows where the player name is the same
    df = df.loc[df["Player"] != player_name]
    if len(player_rows) > 1:
        return player_rows.loc[player_rows["Tm"] == 'TOT'], df

    return player_rows, df


def standardize(df):
    scaler = StandardScaler()
    df.iloc[:, ~df.columns.isin(EXCLUDED_COLUMNS)] = scaler.fit_transform(df.iloc[:, ~df.columns.isin(EXCLUDED_COLUMNS)])
    return df


def get_row_as_float(df, row):
    return row.iloc[0][~row.columns.isin(EXCLUDED_COLUMNS)].values.astype(float)


def calculate_row_similarity(row1, row2, similarity_function):
    if similarity_function == "cosine":
        similarity = cosine_similarity([row1, row2])
        return similarity[0][1]
    elif similarity_function == "pearson":
        corr, _ = pearsonr(row1, row2)
        return corr
    elif similarity_function == "euclidean":
        return -np.linalg.norm(row1 - row2)


def get_most_similar_row(df, row, similarity_function="pearson"):
    max_similarity = []
    # Standardize the data
    df.loc[len(df.index)] = row.iloc[0]
    df = standardize(df)
    row = df.tail(1)
    df.drop(df.tail(1).index, inplace=True)  # drop last n rows

    for i in range(len(df)):
        # Get the row as float
        row1 = get_row_as_float(df, row)
        row2 = get_row_as_float(df, df.iloc[[i]])

        # Calculate similarity
        similarity = calculate_row_similarity(row1, row2, similarity_function)

        compared_player_name = df.iloc[i]["Player"]
        # Update the maximum similarity
        if len(max_similarity) < 3:
            max_similarity.append((similarity, compared_player_name))
        else:
            heapq.heappushpop(max_similarity, (similarity, compared_player_name))
            # print([heapq.heappop(max_similarity) for x in range(len(max_similarity))])
    return [heapq.heappop(max_similarity) for x in range(len(max_similarity))]
