# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов. Напишите программу,
# которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося. Файл состоит из набора строк,
# каждая из которых представляет собой три поля: "Класс Фамилия Рост"
# Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11
# включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего
# требуется вычислить значение в виде вещественного числа. Выводить информацию о среднем росте следует в порядке
# возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо
# вывести напротив него прочерк. В качестве ответа прикрепите файл с полученными данными о среднем росте.

# Sample Input:

# 6	Вяххи	159
# 11	Федотов	172
# 7	Бондарев	158
# 6	Чайкина	153

# Sample Output:
# 1 -
# 2 -
# 3 -
# 4 -
# 5 -
# 6 156.0
# 7 158.0
# 8 -
# 9 -
# 10 -
# 11 172.0


with open(r'dataset_3380_5.txt', 'r', encoding='utf-8') as input_file:
    input_list = []
    for line in input_file:
        input_list.append(line.strip().split('\t'))


input_list1 = [['6', 'Вяххи', '159'], ['11', 'Федотов', '172'], ['7', 'Бондарев', '158'], ['6', 'Чайкина', '153']]


def get_list_of_grades(input=None):
    list_of_grades = {}
    for grade in range(1, 12):
        list_of_grades[grade] = {'height': 0, 'students': 0}
    return list_of_grades


def get_grades_stats(input_list):
    list_of_grades = get_list_of_grades(None)
    for student in input_list:
        list_of_grades[int(student[0])]['height'] += int(student[2])
        list_of_grades[int(student[0])]['students'] += 1
    return list_of_grades


def get_average_height(input_list):
    students_stats = get_grades_stats(input_list)
    avg_height_stats = {}
    for grade in students_stats:
        if students_stats[grade]['students'] == 0:
            avg_height_stats[grade] = '-'
        else:
            avg_height_stats[grade] = students_stats[grade]['height'] / students_stats[grade]['students']
    return avg_height_stats


assert get_average_height(input_list1) == {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: 156.0, 7: 158.0, 8: '-', 9: '-',
                                           10: '-', 11: 172.0}

print('Test passed')


with open(r'result.txt', 'w') as result:
    statistics = get_average_height(input_list)
    for string in statistics:
        result.write(str(string) + ' ' + str(statistics[string]) + '\n')

print('Recording is complete')
