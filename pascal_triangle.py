# Треугольник Паскаля — форма записи биномиальных коэффициентов в виде бесконечной треугольной таблицы.
# Элементы массива обозначаются, где n — номер строки, k — порядковый номер элемента в строке.
# Нумерацию строк начинают с нулевой, при этом нулевая строка — это вершина, то есть число 1.
# Нумерацию чисел в строке также начинают с нуля и с левого края.
# Основная формула для расчета каждого числа в треугольнике имеет вид:
# C(n,k) = C(n - 1, k) - C(n - 1, k - 1)
def get_num_factorial(num):
    if num == 0:
        return 1
    k = 1
    if num == k:
        return num
    else:
        return num * get_num_factorial(num - 1)


def get_num_of_combinations(num, k):
    return int(get_num_factorial(num) / (get_num_factorial(k) * get_num_factorial(num - k)))


def get_n_pascal_triangle_string(n):
    result = []
    for i in range(n + 1):
        result.append(get_num_of_combinations(n, i))
    return result


assert get_n_pascal_triangle_string(0) == [1]
assert get_n_pascal_triangle_string(4) == [1, 4, 6, 4, 1]

print('all tests passed')


# Благодаря функции range() функция, возвращающая факториал числа, без рекурсии пишется даже короче и легче
def get_factorial_num(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
