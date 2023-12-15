# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7

# Sample Input 2:
# 10
# Sample Output 2:
# 10

# put your python code here

# string = input()

def sum_of_neighbours(string: str) -> str:
    '''
    Функция принимает строку из чисел и возвращает новую строку из чисел - сумм соседей каждого исходного числа
    '''
    res_list = [int(num) for num in string.split()]
    result = 'String is empty!'
    if len(res_list) != 0:
        if len(res_list) == 1:
            result = string
            return result
        else:
            subresult = []
            for index in range(len(res_list)):
                if index == len(res_list) - 1:
                    subresult.append(res_list[0] + res_list[-2])
                else:
                    subresult.append(res_list[index - 1] + res_list[index + 1])
                result = ' '.join([str(elem) for elem in subresult])
            return result
    else:
        return result


# print(sum_of_neighbours.__doc__)

assert sum_of_neighbours('1 3 5 6 10') == '13 6 9 15 7'
assert sum_of_neighbours('10') == '10'
assert sum_of_neighbours('') == 'String is empty!'

print('All tests passed :)')
