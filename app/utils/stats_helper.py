from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler
import heapq

EXCLUDED_COLUMNS = ['Player', 'Age', 'Rk', 'Tm', 'G', 'GS', 'Pos']


def get_player_index(df, player):
    return list(np.where(df["Player"] == player)[0])[0]


def standardize(df):
    scaler = StandardScaler()
    df.iloc[:, ~df.columns.isin(EXCLUDED_COLUMNS)] = scaler.fit_transform(df.iloc[:, ~df.columns.isin(EXCLUDED_COLUMNS)])
    return df


def get_row_as_float(df, row):
    return df.iloc[row][~df.columns.isin(EXCLUDED_COLUMNS)].values.astype(float)


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
    df = standardize(df)

    for i in range(len(df)):
        if i == row:
            continue
        # Get the row as float
        row1 = get_row_as_float(df, row)
        row2 = get_row_as_float(df, i)

        # Calculate similarity
        similarity = calculate_row_similarity(row1, row2, similarity_function)

        # Update the maximum similarity
        if len(max_similarity) < 10:
            max_similarity.append((similarity, df.iloc[i]["Player"]))
        else:
            heapq.heappushpop(max_similarity, (similarity, df.iloc[i]["Player"]))

    return [heapq.heappop(max_similarity) for i in range(len(max_similarity))]
