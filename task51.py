# Вашей программе будет доступна функция foo, которая может бросать исключения.
# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError,
# AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
# Пример решения, которое вы должны отправить на проверку.

"""
try:
    foo()
except Exception:
    print("Exception")
except BaseException:
    print("BaseException")
"""
try:  # Что на самом деле является решением задачи
    foo()
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')


# Поскольку у меня нет образцов тех функций foo(), которую запускали в тестах на сайте, пришлось делать самому
def foo(a, b):
    try:
        assert a > b
    except AssertionError:
        print('AssertionError')
    try:
        a / b
    except ZeroDivisionError:
        print("ZeroDivisionError")


def foo1(a, b):
    try:
        a / b
    except ArithmeticError:
        print('ArithmeticError')


foo(0, 1)
foo(1, 0)
foo1(1, 0)
