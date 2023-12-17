# Напишите программу, которая подключает модуль math и, используя значение числа π из этого модуля, находит для
# переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод.

# Sample Input:
# 10.0
# Sample Output:
# 62.83185307179586

import math

radius = float(input())


def circle_length(radius):
    return 2 * radius * math.pi


assert circle_length(10) == 62.83185307179586

print('Test passed')
