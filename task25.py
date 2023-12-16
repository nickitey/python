# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x) = {(1-(x+2)**2, при x <= -2), (-x\2, при -2 < x <= 2), ((x-2)**2 + 1, при х>2)}
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода - вывода.
#
# Sample Input 1:
# 4.5
# Sample Output 1:
# 7.25

# Sample Input 2:
# -4.5
# Sample Output 2:
# -5.25

# Sample Input 3:
# 1
# Sample Output 3:
# -0.5

def f(x):
    # put your python code here
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    else:
        return (x - 2) ** 2 + 1


assert f(4.5) == 7.25
assert f(-4.5) == -5.25
assert f(1) == -0.5

print('All tests passed')


def f(x):
    # put your python code here
    def f1(x):
        if x:
            return 1 - (x + 2) ** 2
        else:
            return "Мсье знает толк в извращениях1"

    def f2(x):
        if x:
            return -x / 2
        else:
            return "Мсье знает толк в извращениях2"

    def f3(x):
        if x:
            return (x - 2) ** 2 + 1
        else:
            return "Мсье знает толк в извращениях3"

    if x:
        if x <= -2:
            return f1
        elif -2 < x <= 2:
            return f2
        else:
            return f3
    else:
        return "Мсье знает толк в извращениях0"


assert f(4.5)(4.5) == 7.25
assert f(-4.5)(-4.5) == -5.25
assert f(1)(1) == -0.5
assert f(None) == "Мсье знает толк в извращениях0"
assert f(-3)(None) == "Мсье знает толк в извращениях1"
assert f(1)(None) == "Мсье знает толк в извращениях2"
assert f(3)(None) == "Мсье знает толк в извращениях3"

print('All tests passed')
