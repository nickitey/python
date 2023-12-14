# Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
# Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4

# Sample Input 2:
# 10
# Sample Output 2:

# Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3

# Sample Input 4:
# 1 1 1 1 1 2 2 2
# Sample Output 4:
# 1 2

# put your python code here

""" Сначала я решил эту задачу старым способом, но мне он тоже не нравился
def repeat_in_string(string: str) -> str:
    result = 'String is empty!'
    sub_result = sorted([int(elem) for elem in string.split()])
    if len(sub_result) != 0:
        if len(sub_result) == 1:
            result = ''
            return result
        else:
            result = []
            amount = 1
            start_index = 1
            list_interval = sub_result[start_index:start_index + 1]
            for elem in sub_result:
                if elem in list_interval:
                    amount += 1
                else:
                    if amount > 1:
                        result.append(elem)
                        amount = 1
                start_index += 1
                list_interval = sub_result[start_index:start_index + 1]
            return ' '.join([str(elem) for elem in result])
    else:
        return result
"""


# string = input()

def repeat_in_string(string: str) -> str:  # Потом я подумал и решил найти другой способ решения
    '''
    Возвращает строку из неуникальных элементов исходной строки
    '''
    result = 'String is empty!'
    sub_result = sorted([int(elem) for elem in string.split()])
    if len(sub_result) != 0:
        if len(sub_result) == 1:
            result = ''
            return result
        else:
            result = []
            amount = 0
            sub_list_elem = []
            for index in range(len(sub_result)):
                for elem in sub_result:
                    # Вариант без слайсинга:
                    # temp_list = []
                    # temp_list.append(sub_result)
                    # Слайсинг здесь удобен тем, что сразу возвращает список.
                    # Если просто перебирать по индексам, то нужно использовать
                    # `временный` пустой список, куда помещать перебираемый элемент.
                    # В противном случае интерпретатор ругается, что int - не итерируемый объект (что логично).
                    if elem in sub_result[index:index + 1]:
                        # Соответственно проверка должна происходить в temp_list
                        amount += 1
                    else:
                        if amount > 1 and (sub_result[index] not in result):
                            result.append(sub_result[index])
                        amount = 0
                    # А в конце цикла нужно очищать временный список:
                    # del temp_list[0]
            return ' '.join([str(elem) for elem in result])
    else:
        return result


# print(repeat_in_string.__doc__)

assert repeat_in_string('4 8 0 3 4 2 0 3') == '0 3 4'
assert repeat_in_string('10') == ''
assert repeat_in_string('1 1 2 2 3 3') == '1 2 3'
assert repeat_in_string('1 1 1 1 1 2 2 2') == '1 2'
assert repeat_in_string('') == 'String is empty!'

print('All tests passed :)')
