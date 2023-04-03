from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.stats import pearsonr
from sklearn.preprocessing import StandardScaler


def get_player_index(df, player):
    return list(np.where(df["Player"] == player)[0])[0]


def get_most_similar_row_cosine(df, row):
    max_similarity = 0
    most_similar = None

    scaler = StandardScaler()
    df.iloc[:, 7:] = scaler.fit_transform(df.iloc[:, 7:])

    for i in range(len(df)):
        if i == row:
            continue
        row1 = df.iloc[row][7:].values.astype(float)
        row2 = df.iloc[i][7:].values.astype(float)

        # Calculate cosine similarity
        similarity = cosine_similarity([row1, row2])

        # Update the maximum similarity
        if similarity[0][1] > max_similarity:
            max_similarity = similarity[0][1]
            most_similar = f'{df.iloc[row]["Player"]} and {df.iloc[i]["Player"]} are {similarity[0][1]} similar'
    return most_similar


def get_most_similar_row_euclidean(df, row):
    min_distance = float('inf')
    most_similar = None
    scaler = StandardScaler()
    df.iloc[:, 7:] = scaler.fit_transform(df.iloc[:, 7:])
    for i in range(len(df)):
        if i == row:
            continue
        row1 = df.iloc[row][7:].values.astype(float)
        row2 = df.iloc[i][7:].values.astype(float)
        distance = np.linalg.norm(row1 - row2)
        if distance < min_distance:
            min_distance = distance
            most_similar = f'{df.iloc[row]["Player"]} and {df.iloc[i]["Player"]} are {distance} similar'
        print(f'{df.iloc[row]["Player"]} and {df.iloc[i]["Player"]} are {distance} similar')

    return most_similar


def get_most_similar_row_pearsonian(df, row):
    max_similarity = 0
    most_similar = None
    scaler = StandardScaler()
    df.iloc[:, 7:] = scaler.fit_transform(df.iloc[:, 7:])

    for i in range(len(df)):
        if i == row:
            continue
        row1 = df.iloc[row][7:].values.astype(float)
        row2 = df.iloc[i][7:].values.astype(float)

        # Calculate pearson correlation
        corr, _ = pearsonr(row1, row2)


        # Update the maximum similarity
        if corr > max_similarity:
            max_similarity = corr
            most_similar = f'{df.iloc[row]["Player"]} and {df.iloc[i]["Player"]} are {corr} similar'
    return most_similar


