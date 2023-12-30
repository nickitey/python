# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт
# об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
# Пример входного файла:
# 31
# 999
# 1024
# 502

# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring


import requests


def is_number_interesting(number):
    url = f'http://numbersapi.com/{number}/math'
    response = requests.get(url, params='json').json()
    if response['found']:
        return 'Interesting'
    else:
        return 'Boring'


numbers_list = []

with open(r'dataset_24476_3.txt', 'r') as numbers_file:
    for string in numbers_file:
        numbers_list.append(int(string.strip()))

with open(r'result.txt', 'w') as result:
    for number in numbers_list:
        result.write(f'{str(is_number_interesting(number))}\n')
