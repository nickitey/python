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

""" # Вариант ручного ввода каждой строки
n = int(input())
input_list = []
while len(input_list) < n:
    game = input().strip().split(';')
    input_list.append(game)
"""

""" # Готовый вариант ввода, на котором без лишней мозгоебли проверял код
input_list2 = [ 
    ['Бенедикт', '9', 'Камбербетч', '10'],
    ['Локомотив', '12', 'Зенит', '3'],
    ['Спартак', '8', 'Локомотив', '15'],
    ['Динамо', '9', 'Зенит', '15'],
    ['Камбербетч', '8', 'Локомотив', '11'],
    ['Динамо', '15', 'Спартак', '30'],
]
"""

# Последний использованный вариант ввода, заодно потренировался в чтении из файла
with open(r'input.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.readlines()
    n = int(input_text[0])
    input_list = []  # Можно было бы просто перебрать исходный список и каждую строку превратить в список.
    # Но если матчей было больше, чем первое число на входе? Ну типа там какие-нибудь товарищеские матчи на ввод попали
    for line_index in range(1, n + 1):
        input_list.append(input_text[line_index].strip().split(';'))


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
        result[team] = {'games': games_count[team], 'wins': 0, 'equals': 0, 'loses': 0}
    return result


def get_teams_stats(input_list):
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
                elif game[2] == team:
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
                stats.append(results[team][stat])
            elif stat == 'wins':
                stats.append(results[team][stat])
                points += results[team][stat] * 3
            elif stat == 'equals':
                stats.append(results[team][stat])
                points += results[team][stat]
            else:
                stats.append(results[team][stat])
        stats.append(points)
        result_list[team] = stats  # ' '.join([str(i) for i in stats]) - изначально я предпочитал сразу превращать все
        # статы команды в строку, но любезно предоставленный кем-то ожидаемый результат работы программы представлял
        # статы в виде списка, пришлось соглашаться
    return result_list


# Данные для теста взяты отсюда https://stepik.org/lesson/3380/step/1?discussion=273585&unit=963
assert get_championship_result(input_list) == {'Польша': [3, 2, 1, 0, 7], 'Россия': [3, 0, 1, 2, 1],
                                               'Хорватия': [3, 1, 1, 1, 4], 'Уэльс': [3, 2, 0, 1, 6],
                                               'Франция': [3, 1, 2, 0, 5], 'Исландия': [3, 1, 2, 0, 5],
                                               'Румыния': [3, 0, 2, 1, 2], 'Испания': [3, 3, 0, 0, 9],
                                               'Австрия': [3, 0, 1, 2, 1], 'Португалия': [3, 1, 2, 0, 5],
                                               'Швеция': [2, 0, 1, 1, 1], 'Словакия': [3, 1, 1, 1, 4],
                                               'Чехия': [3, 0, 1, 2, 1], 'Италия': [3, 3, 0, 0, 9],
                                               'Англия': [3, 1, 2, 0, 5], 'Германия': [3, 2, 1, 0, 7],
                                               'Бельгия': [3, 1, 1, 1, 4], 'Северная Ирландия': [3, 1, 0, 2, 3],
                                               'Турция': [3, 1, 0, 2, 3], 'Украина': [3, 0, 0, 3, 0],
                                               'Албания': [3, 1, 0, 2, 3], 'Швейцария': [3, 1, 2, 0, 5],
                                               'Венгрия': [3, 1, 1, 1, 4], 'Ирландия': [2, 0, 0, 2, 0]}

print('test passed')

"""
iterator = get_championship_result(input_list)
for string in iterator:
    print(string, iterator[string], sep=':')
"""  # Тесты на сайте требовали вывести на экран результаты работы программы
