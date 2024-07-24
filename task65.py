# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит
# список имен прямых предков.

# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Эквивалент на Python:
"""
class A:
    pass

class B(A, C):
    pass

class C(A):
    pass
"""
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс
# не наследуется явно от одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

# Ща батя вам покажет, как json'ы разворачивать надо

import json

input_json = json.dumps([{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, 
                         {"name": "C", "parents": ["A"]}])


def count_anscestors_amount(json_file):
    json_python_obj = json.loads(json_file)
    anscestors_list = {}
    for class_name in json_python_obj:
        print(class_name)
        for parent in class_name['parents']:
            if parent in anscestors_list:
                anscestors_list[parent] += 1
            else:
                anscestors_list[parent] = 1
    print(anscestors_list)




count_anscestors_amount(input_json)
#assert count_anscestors_amount(input_json) == {'A' : 3, 'B' : 1, 'C' : 2}
#print('YOU SHALL NOT PASS! But tests passed')
