# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n —
# столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел,
# записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4

# put your python code here

def get_str_of_nums(integer):
    """
    Функция принимает целое положительное число i и возвращает строку длиной i с возрастающей
    последовательностью целых положительных чисел, где каждое число n повторяется n раз.
    """
    result = ''
    if integer > 0 and (integer // 1 == integer):
        res_list = []
        current = 1
        amount = 0
        while len(res_list) < integer:
            if amount < current:
                res_list.append(current)
                amount += 1
            else:
                current += 1
                amount = 0
        result = ' '.join(str(elem) for elem in res_list)
        return result
    else:
       return result


# print(get_str_of_nums.__doc__)

assert get_str_of_nums(7) == '1 2 2 3 3 3 4'
assert get_str_of_nums(0) == ''
assert get_str_of_nums(-1) == ''
assert get_str_of_nums(2.25) == ''
assert get_str_of_nums(28) == '1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7'
assert get_str_of_nums(55) == ('1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7 8 8 8 8 8 8 8 8 9 9 9 9 9 9 9 '
                               '9 9 10 10 10 10 10 10 10 10 10 10')

print('All tests passed :)')
