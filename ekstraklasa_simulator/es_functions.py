# functions fo ekstraklasa_simulator
# Maciej Błażejczak MBQA
import random


def generate_games():
    """
    Function to generate pairs of games between teams
    :return:
        list: games - list of games between teams
    """
    teams = ["Rakow Czestochowa", "Legia Warszawa", "Lech Poznan", "Widzew Lodz", "Pogon Szczecin", "Cracovia Krakow",
             "Warta Poznan", "Radomiak Radom", "Stal Mielec", "Slask Wroclaw", "Zaglebie Lubin", "Wisla Plock",
             "Piast Gliwice", "Jagiellonia Bialystok", "Gornik Zabrze", "Korona Kielce", "Lechia Gdansk",
             "Miedz Legnica"]
    counter = len(teams)
    all_games = []
    game_schedule = []
    while counter > 0:
        my_team = teams[counter - 1]
        for team in teams:
            if team != my_team:
                game_schedule.append([my_team, team])
                game_schedule.append([team, my_team])
        all_games.append(game_schedule)
        counter -= 1
        # remove duplicates from all_games
    temp_game_container = []
    games = []
    for game in all_games:
        if isinstance(game, list):
            for n in game:
                temp_game_container.append(n)
    for game in temp_game_container:
        if game not in games:
            games.append(game)

    return games


def generate_score():
    """
    Function to generate game score
    :return:
        int: score for team1
        int: score for team2
    """
    team1 = random.randint(0, 3)
    team2 = random.randint(0, 3)
    return team1, team2


def count_points(list, point):
    """
    Function to calculate points
    :param list: list of winners or draws
    :param point: 3 point in case of win, 1 point in case of draw, 1 point in case of failure
    :return: dictionary sorted by value
    """
    result = {}
    for item in list:
        key = item
        value = list.count(item) * point
        result.update({key: value})

    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    return result


def create_final_table(winners, draws):
    """
    Function to create a final table (winners and draws)
    :param winners: dictionary with winners
    :param draws: dictionary with draws
    :return: dictionary sorted by value
    """
    final_table_list = []

    for key, value in winners.items():
        if key in draws:
            key = key
            value = winners[key] + draws[key]
            final_table_list.append([key, value])
    final_table_list = sorted(final_table_list, key=lambda x: x[1], reverse=True)
    champion = ['👑 WINNER 👑']
    relegation = ['RELEGATION']

    final_table_list[0] = final_table_list[0] + champion
    final_table_list[-1] = final_table_list[-1] + relegation
    final_table_list[-2] = final_table_list[-2] + relegation
    final_table_list[-3] = final_table_list[-3] + relegation

    return final_table_list


def create_losers_table(losers):
    """
    Function to create a losers table
    :param losers: dictionary with losers
    :return: dictionary sorted by value
    """
    losers_table = []

    for key, value in losers.items():
        losers_table.append([key, value])
    losers_table = sorted(losers_table, key=lambda x: x[1], reverse=True)
    looser = ['👑 THE BIGGEST LOSER 👑']
    losers_table[0] = losers_table[0] + looser

    return losers_table
