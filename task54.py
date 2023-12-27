# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число
# дней, равное days.
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.

# Sample Input 1:
# 2016 4 20
# 14
# Sample Output 1:
# 2016 5 4

# Sample Input 2:
# 2016 2 20
# 9
# Sample Output 2:
# 2016 2 29

# Sample Input 3:
# 2015 12 31
# 1
# Sample Output 3:
# 2016 1 1


import datetime


"""
days = (tuple(int(i) for i in input().split(' ')))
n = int(input())
date = datetime.date(*days)
next_date = (date + datetime.timedelta(days=n))
for i in str(next_date.split('-'):
    print(int(i), end=' ')
"""


def get_date_from_str(string):
    return tuple(int(i) for i in string.split(' '))


def get_next_time(string, n):
    date = datetime.date(*get_date_from_str(string))
    return date + datetime.timedelta(days=n)


assert str(get_next_time('2016 4 20', 14)) == '2016-05-04'
assert str(get_next_time('2016 2 20', 9)) == '2016-02-29'
assert str(get_next_time('2015 12 31', 1)) == '2016-01-01'

print('It\'s ok')
