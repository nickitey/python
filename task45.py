# Реализуйте программу, которая будет эмулировать работу с пространствами имен.
# Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var>
# при запросе из пространства <namespace>, или None, если такого пространства не существует

# Рассмотрим набор запросов
# add global a
# create foo global
# add foo b
# create bar foo
# add bar a

# Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен,
# созданной при выполнении данного кода
# a = 0
# def foo():
#  b = 1
#  def bar():
#    a = 2
# В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global.
# Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри
# пространства global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции
# foo функцию bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.

# Добавим запросы get к нашим запросам
# get foo a
# get foo c
# get bar a
# get bar b
# Представим как это могло бы выглядеть в коде
# a = 0
# def foo():
#  b = 1
#  get(a)
#  get(c)
#  def bar():
#    a = 2
#    get(a)
#    get(b)
# Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
# Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a,
# но в пространстве global, внутри которого находится пространство foo, она объявлена.
# Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

# Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global
# не была объявлена переменная с.

# Более формально, результатом работы get <namespace> <var> является <namespace>, если в пространстве <namespace>
# была объявлена переменная <var>
# get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>,
# если переменная не была объявлена
# None, если не существует <parent>, т. е. <namespace> – это global

# Формат входных данных
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных
# латинских букв.

# Формат выходных данных
# Для каждого запроса get выведите в отдельной строке его результат.

# Sample Input:
# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b
# Sample Output:
# global
# None
# bar
# foo


"""
length = int(input())
input_list = []
while len(input_list) < length:
    command = input().split(' ')
    input_list.append(command)
"""

input_list1 = [['add', 'global', 'a'], ['create', 'foo', 'global'], ['add', 'foo', 'b'], ['get', 'foo', 'a'],
              ['get', 'foo', 'c'], ['create', 'bar', 'foo'], ['add', 'bar', 'a'], ['get', 'bar', 'a'],
              ['get', 'bar', 'b']]
input_list2 = [['create', 'foo', 'global'], ['add', 'foo', 'a'], ['get', 'global', 'a']]
input_list3 = [['create', 'first', 'global'], ['create', 'second', 'first'], ['create', 'third', 'second'],
               ['add', 'first', 'my_var'], ['get', 'third', 'my_var']]
input_list4 = [['add', 'global', 'a'], ['create', 'foo1', 'global'], ['create', 'foo2', 'global'],
               ['create', 'bar1', 'foo1'], ['create', 'bar2', 'foo2'], ['create', 'new1', 'bar1'],
               ['create', 'new2', 'bar2'], ['add', 'global', 'b'], ['add', 'foo1', 'a'], ['add', 'foo2', 'b'],
               ['add', 'bar1', 'a'], ['add', 'bar2', 'b'], ['add', 'new1', 'a'], ['add', 'new2', 'b'],
               ['get', 'new1', 'b']]
input_list5 = [['create', 'foo', 'global'], ['create', 'bar', 'foo'], ['add', 'global', 'a'], ['add', 'foo', 'a'],
               ['add', 'bar', 'c'], ['get', 'global', 'c']]
input_list6 = [['create', 'foo', 'global'], ['create', 'bar', 'foo'], ['create', 'barz', 'bar'],
               ['create', 'bary', 'barz'], ['add', 'bar', 'b'], ['create', 'zoo', 'bar'], ['create', 'zoo2', 'zoo'],
               ['create', 'zoo3', 'zoo2'], ['add', 'bary', 'b'], ['create', 'doo', 'zoo'], ['get', 'zoo', 'b']]


def get_namespace_name(input_list):
    def find_namespace(scope, space, variable):
        if variable in scope[space]['variables']:
            return space
        elif scope[space]['parent'] is None:
            return None
        else:
            return find_namespace(scope, scope[space]['parent'], variable)

    namespaces = {'global': {
        'variables': [],
        'parent': None
    }}
    result = []

    for command in input_list:
        if command[0] == 'create':
            namespaces[command[2]]['variables'].append(command[1])
            namespaces[command[1]] = {'variables': [],
                                      'parent': command[2]}
        if command[0] == 'add':
            namespaces[command[1]]['variables'].append(command[2])
        if command[0] == 'get':
            result.append(find_namespace(namespaces, command[1], command[2]))
    return result


assert get_namespace_name(input_list1) == ['global', None, 'bar', 'foo']
assert get_namespace_name(input_list2) == [None]
assert get_namespace_name(input_list3) == ['first']
assert get_namespace_name(input_list4) == ['global']
assert get_namespace_name(input_list5) == [None]
assert get_namespace_name(input_list6) == ['bar']

print('passed!')
