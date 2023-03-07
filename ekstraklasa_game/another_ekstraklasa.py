# generate pairs of games between all ekstraklasa teams (season 2022/23)
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
        int:
    """
    team1 = random.randint(0, 3)
    team2 = random.randint(0, 3)
    return team1, team2


games = generate_games()

results = []
for game in games:
    team1, team2 = generate_score()
    results.append([game, team1, team2])
print(results)


# results = [[['Miedz Legnica', 'Rakow Czestochowa'], 0, 3], [['Rakow Czestochowa', 'Miedz Legnica'], 1, 1]]
winner = []
looser = []
draw = []

for n in results:
    if n[1] > n[2]:
        winner.append(n[0][0])
        looser.append(n[0][1])
    elif n[1] < n[2]:
        winner.append(n[0][1])
        looser.append(n[0][0])
    else:
        draw.append(n[0][0])
        draw.append(n[0][1])

print("Winner: ", winner)
print("Looser: ", looser)
print("Draw: ", draw)
