# generate pairs of games between random picked team and other teams
# Maciej Błażejczak MBQA

import random


def generate_games():
    """
    Function to generate pairs of games between randomly picked team and other teams
    :return:
        str: my_team - randomly picked team
        list: game_schedule - games between my_team and other teams
    """
    teams = ["Rakow Czestochowa", "Legia Warszawa", "Lech Poznan", "Widzew Lodz", "Pogon Szczecin", "Cracovia Krakow",
             "Warta Poznan", "Radomiak Radom", "Stal Mielec", "Slask Wroclaw", "Zaglebie Lubin", "Wisla Plock",
             "Piast Gliwice", "Jagiellonia Bialystok", "Gornik Zabrze", "Korona Kielce", "Lechia Gdansk",
             "Miedz Legnica"]
    my_team = random.choice(teams)
    teams.remove(my_team)
    game_schedule = []
    for team in teams:
        game_schedule.append([my_team, team])
        game_schedule.append([team, my_team])

    return my_team, game_schedule


chosen_team, games = generate_games()
print(f"Team: {chosen_team}")
print(f"Games: {games}")
