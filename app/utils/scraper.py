from bs4 import BeautifulSoup
import requests
import string
import random
import pandas as pd

CURRENT_YEAR = 2023

def make_soup(url):
    res = requests.get(url)
    if res.status_code != 200:
        if res.status_code == 429:
            raise Exception(res.headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def get_player_table(soup):
    table = soup.find('table', id="players")
    rows = table.find_all('tr')
    return rows


def get_random_player():
    """Get random player route"""
    random_letter = random.choice(string.ascii_lowercase)
    url = f'https://www.basketball-reference.com/players/{random_letter}/'
    soup = make_soup(url)
    rows = get_player_table(soup)
    # get random player
    random_player = random.choice(rows)
    # get player name
    player_name = random_player.find('th', {'data-stat': 'player'}).text
    return player_name



def filter_players_by_retirement_year(player_row, year):
    """Get random player route"""
    if player_row.find('td', {'data-stat': 'year_max'}) is None:
        return False
    player_retirement_year = player_row.find('td', {'data-stat': 'year_max'}).text
    return int(player_retirement_year) >= year

def get_random_active_player():
    """Get random active player route"""
    random_letter = random.choice(string.ascii_lowercase)
    url = f'https://www.basketball-reference.com/players/{random_letter}/'
    # try:
    soup = make_soup(url)
    rows = get_player_table(soup)
    # get random player
    filtered_rows = list(filter(lambda row: filter_players_by_retirement_year(row, CURRENT_YEAR), rows))
    random_player = random.choice(filtered_rows)
    player_name = random_player.find('th', {'data-stat': 'player'}).text
    return player_name

def get_season_stats_as_df(season):
    """Get season stats route"""
    url = f'https://www.basketball-reference.com/leagues/NBA_{season}_per_poss.html'
    soup = make_soup(url)
    table = soup.find('table', id="per_poss_stats")
    df = pd.read_html(str(table))[0]
    # remove header rows in middle of table
    df = df[df['Age'] != 'Age']
    return df.fillna(0)