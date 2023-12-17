# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом
# и вывести получившуюся статистику. Программа должна считывать одну строку со стандартного ввода и выводить
# для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
# (см. пример вывода). Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться
# только один раз.

# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2

# Sample Input 2:
# a A a
# Sample Output 2:
# a 3

"""word = input() # Все, как учил, сенсей: ввод отдельно, функция отдельно
string = ''
"""


def count_words(string):
    """
    Функция принимает строку, разбивает ее на массив слов (по пробелу), возвращает количество каждого слова в строке
    """
    result = {}
    word_list = string.split(' ')
    for word in word_list:
        if word.lower() in result:
            result[word.lower()] += 1
        else:
            result[word.lower()] = 1
    """for word in result:              # На самом деле авторы задачи хотят от меня этого, а не возвращать весь словать
        print(word, result.get(word))"""
    return result


# print(count_words.__doc__) # Предварительно убедился что второй закомментированный блок
# (или тут принято говорить `задокументированный`?) не попал в документацию к функции

assert count_words('a aa abC aa ac abc bcd a') == {'ac': 1, 'a': 2, 'abc': 2, 'bcd': 1, 'aa': 2}
assert count_words('a A a') == {'a': 3}

print('All tests passed')


def count_words(string):
    """
    Функция принимает строку, разбивает ее на массив слов (по пробелу), возвращает количество каждого слова в строке
    """
    result = {}
    word_list = string.split(' ')
    for word in word_list:
        word = word.lower()
        if word in result:
            # лишние повторные вычисления
            result[word] += 1
        else:
            result[word] = 1
    """for word in result:              # На самом деле авторы задачи хотят от меня этого, а не возвращать весь словать
        print(word, result.get(word))"""
    return result


assert count_words('a aa abC aa ac abc bcd a') == {'ac': 1, 'a': 2, 'abc': 2, 'bcd': 1, 'aa': 2}
assert count_words('a A a') == {'a': 3}

print('All tests passed')
