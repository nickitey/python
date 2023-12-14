# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать
# не нужно. В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю
# и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.

# Sample Input:
# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# Sample Output:
# 340

# put your python code here

def sum_of_quads(*string: str) -> int | str:
    """
    Функция принимает на ввод строки с числами и накапливает их до тех пор, пока их общая сумма не станет равна 0,
    после чего возвращает сумму квадратов чисел, дающих в сумме 0. Остальные строки игнорируются.
    """
    result = 0
    if string != ('',):
        if string == ('0',):
            return result
        else:
            res_list = []
            sum_list = list(string)
            sub_sum = 0
            for summand in sum_list:
                sub_sum += int(summand)
                res_list.append(summand)
                if sub_sum == 0:
                    break
            for unit in res_list:
                result += (int(unit) ** 2)
        return result
    else:
        return "Input is empty!"


# print(sum_of_quads.__doc__)

assert sum_of_quads('1', '-3', '5', '-6', '-10', '13', '4', '-8') == 340
assert sum_of_quads('0') == 0
assert sum_of_quads('0', '0', '0') == 0
assert sum_of_quads('4', '3', '-7', '82', '-19') == 74
assert sum_of_quads('-950', '143', '216', '-311', '513', '27', '215', '147', '231') == 1398058
assert sum_of_quads('') == 'Input is empty!'

print('All tests passed :)')
