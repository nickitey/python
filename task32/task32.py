# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке
# записана следующая информация: Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку Поля внутри
# строки разделены точкой с запятой, оценки — целые числа. Напишите программу, которая считывает исходный файл с
# подобной структурой и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом. Также вычислите средние баллы по математике, физике и русскому
# языку по всем абитуриентам и добавьте полученные значения, разделённые пробелом, последней строкой в файл с
# ответом. В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной
# строкой со средними оценками по трём предметам.

# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
# print('First;Second-1 Second-2;Third'.split(';')) ['First',
# 'Second-1 Second-2', 'Third']

# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

with open(r'dataset_3363_4.txt', 'r', encoding='utf-8') as input_file:
    input_list = []
    for line in input_file:
        line = line.strip().split(';')
        input_list.append(line[1:len(line)])


def get_average_marks(marks):
    max_stud_mark = 0
    average_subj_marks = []
    average_stud_marks = []
    max_subj_marks = {}
    for student in marks:
        for subject in range(len(student)):
            max_stud_mark += int(student[subject])
            if subject in max_subj_marks:
                max_subj_marks[subject] += int(student[subject])
            else:
                max_subj_marks[subject] = int(student[subject])
        average_stud_marks.append(max_stud_mark / len(student))
        max_stud_mark = 0
    for subject in max_subj_marks:
        average_subj_marks.append(str(max_subj_marks.get(subject) / len(marks)))
    return average_stud_marks, ' '.join(average_subj_marks)


def get_avg_std_mark(marks):
    max_stud_mark = 0
    average_stud_marks = []
    for student in marks:
        for subject in range(len(student)):
            max_stud_mark += int(student[subject])
        average_stud_marks.append(max_stud_mark / len(student))
        max_stud_mark = 0
    return average_stud_marks


def get_avg_subj_mark(marks):
    average_subj_marks = []
    max_subj_marks = {}
    for student in marks:
        for subject in range(len(student)):
            if subject in max_subj_marks:
                max_subj_marks[subject] += int(student[subject])
            else:
                max_subj_marks[subject] = int(student[subject])
    for subject in max_subj_marks:
        average_subj_marks.append(str(max_subj_marks.get(subject) / len(marks)))
    return ' '.join(average_subj_marks)


with open('result.txt', 'w') as res:
    for string in get_avg_std_mark(input_list):
        res.write(str(string) + '\n')
    res.write(get_avg_subj_mark(input_list))