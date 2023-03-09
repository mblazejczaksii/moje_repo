# simulate ekstraklasa season
# Maciej Błażejczak MBQA
from tabulate import tabulate
from es_functions import generate_games, generate_score, count_points, create_final_table, create_losers_table

# generate all possible games between teams
games = generate_games()

# generate score for all games
results = []
for game in games:
    team1, team2 = generate_score()
    results.append([game, team1, team2])

# assign results to teams
winners = []
losers = []
draws = []
for n in results:
    if n[1] > n[2]:
        winners.append(n[0][0])
        losers.append(n[0][1])
    elif n[1] < n[2]:
        winners.append(n[0][1])
        losers.append(n[0][0])
    else:
        draws.append(n[0][0])
        draws.append(n[0][1])

# counting points and create final table
winners = count_points(list=winners, point=3)
draws = count_points(list=draws, point=1)
losers = count_points(list=losers, point=1)
final_table_list = create_final_table(winners=winners, draws=draws)
losers_table = create_losers_table(losers=losers)

# define header names and display final table
col_names = ["Team", "Points", "Decision"]
print(tabulate(final_table_list, headers=col_names))
print("\n")
# define header names and display losers table
col_names = ["Team", "Loses", "Decision"]
print(tabulate(losers_table, headers=col_names))
