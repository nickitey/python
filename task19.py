# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел.
# Используйте метод split строки.

# Sample Input:
# 4 -1 9 3
# Sample Output:
# 15

# put your python code here

# string = input()
# Пока платформа требует от меня не функции, а просто блоки кода, задачи решаются с вводом значений с клавиатуры
def sum_for_input(string: str) -> int:
    '''
    Возвращает сумму чисел - элементов строки
    '''
    summary = 0
    summands = [int(elem) for elem in string.split()]
    for summand in summands:
        summary += summand

    return summary

# print(sum_for_input.__doc__) # Это очень прикольно. Я специально это не буду убирать, чтобы видеть и запомнить

assert sum_for_input('4 -1 9 3') == 15
assert sum_for_input('1 -1 1 -1') == 0
assert sum_for_input('1000 100 10 1') == 1111

print('All tests passed :)')