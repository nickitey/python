# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
# выводит на стандартный вывод сводную таблицу результатов всех матчей. За победу команде начисляется 3 очка,
# за поражение — 0, за ничью — 1. Формат ввода следующий: В первой строке указано целое число n — количество
# завершенных игр. После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.

# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

"""
n = int(input())
input_list = []
while len(input_list) < n:
    game = input().split(';')
    input_list.append(game)
"""

input_list = [
    ['Спартак', '9', 'Зенит', '10'],
    ['Локомотив', '12', 'Зенит', '3'],
    ['Спартак', '8', 'Локомотив', '15']
]

input_list2 = [
    ['Бенедикт', '9', 'Камбербетч', '10'],
    ['Локомотив', '12', 'Зенит', '3'],
    ['Спартак', '8', 'Локомотив', '15'],
    ['Динамо', '9', 'Зенит', '15'],
    ['Камбербетч', '8', 'Локомотив', '11'],
    ['Динамо', '15', 'Спартак', '30'],
]


def get_teams_list(input_list):
    result = set()
    for game in input_list:
        for order in range(len(game)):
            if order % 2 == 0:
                result.add(game[order])
    return result


def get_count_games(input_list):
    teams_list = get_teams_list(input_list)
    teams_count = {}
    for team in teams_list:
        teams_count[team] = 0
    for game in input_list:
        for item in game:
            if item in teams_list:
                teams_count[item] += 1
    return teams_count


def get_result_template(input_list):
    teams_list = get_teams_list(input_list)
    games_count = get_count_games(input_list)
    result = {}
    for team in teams_list:
        result[team] = {'wins': 0, 'equals': 0, 'loses': 0}
        result[team]['games'] = games_count[team]
    return result


def get_teams_stats(input_list):
    teams_list = get_teams_list(input_list)
    stats_table = get_result_template(input_list)
    for game in input_list:
        if int(game[1]) > int(game[3]):
            for team in stats_table:
                if game[0] == team:
                    stats_table[team]['wins'] += 1
                elif game[2] == team:
                    stats_table[team]['loses'] += 1
        elif int(game[1]) == int(game[3]):
            for team in stats_table:
                if game[0] == team:
                    stats_table[team]['equals'] += 1
                elif game[0] == team:
                    stats_table[team]['equals'] += 1
        else:
            for team in stats_table:
                if game[0] == team:
                    stats_table[team]['loses'] += 1
                elif game[2] == team:
                    stats_table[team]['wins'] += 1
    return stats_table


def get_championship_result(input_list):
    results = get_teams_stats(input_list)
    result_list = {}
    for team in results:
        stats = []
        points = 0
        for stat in results[team]:
            if stat == 'games':
                stats.insert(0, results[team][stat])
            elif stat == 'wins':
                stats.append(results[team][stat])
                points += results[team][stat] * 3
            elif stat == 'equals':
                stats.append(results[team][stat])
                points += results[team][stat]
            else:
                stats.append(results[team][stat])
        stats.append(points)
        result_list[team] = ' '.join([str(i) for i in stats])
    return result_list


iterator = get_championship_result(input_list2)
for string in iterator:
    print(string, iterator[string], sep=':')

# По-моему, я получил то, что от меня хотели. Но тесты на сайте я не прошел)