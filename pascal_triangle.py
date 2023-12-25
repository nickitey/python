# Треугольник Паскаля — форма записи биномиальных коэффициентов в виде бесконечной треугольной таблицы.
# Элементы массива обозначаются, где n — номер строки, k — порядковый номер элемента в строке.
# Нумерацию строк начинают с нулевой, при этом нулевая строка — это вершина, то есть число 1.
# Нумерацию чисел в строке также начинают с нуля и с левого края.
# Основная формула для расчета каждого числа в треугольнике имеет вид:
# C(n,k) = C(n - 1, k) - C(n - 1, k - 1)


# Земельный кодекс Российской Федерации.
# Статья 5. Часть 3:
# Для целей настоящего Кодекса используются следующие понятия и определения:
# собственники земельных участков - лица, являющиеся собственниками земельных участков
def get_num_factorial(num):
    if num == 0:
        return 1
    k = 1
    if num == k:
        return num
    else:
        return num * get_num_factorial(num - 1)


def get_amount_of_combinations(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return get_amount_of_combinations(n - 1, k) + get_amount_of_combinations(n - 1, k - 1)


def get_n_pascal_triangle_string(n):
    result = []
    for i in range(n + 1):
        result.append(get_amount_of_combinations(n, i))
    return result


assert get_n_pascal_triangle_string(0) == [1]
assert get_n_pascal_triangle_string(4) == [1, 4, 6, 4, 1]

print('all tests passed')


# А ТЕПЕРЬ БЕЗ РЕКУРСИИ!
def get_factorial_num(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def get_num_of_combinations(num, k):
    return int(get_factorial_num(num) / (get_factorial_num(k) * get_factorial_num(num - k)))


def get_nth_pascal_triangle_string(n):
    result = []
    for i in range(n + 1):
        result.append(get_num_of_combinations(n, i))
    return result


assert get_nth_pascal_triangle_string(0) == [1]
assert get_nth_pascal_triangle_string(4) == [1, 4, 6, 4, 1]

print('These tests also passed')
