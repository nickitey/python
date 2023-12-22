# Простейшая система проверки орфографии может быть основана на использовании списка известных слов. Если введённое
# слово не найдено в этом списке, оно помечается как "ошибка". Попробуем написать подобную систему. На вход программе
# первой строкой передаётся количество d известных нам слов, после чего на d строках указываются эти слова. Затем
# передаётся количество l строк текста для проверки, после чего l строк текста. Выведите уникальные "ошибки" в
# произвольном порядке. Работу производите без учёта регистра.

# Sample Input:
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic
# Sample Output:
# stepic
# champignons
# the

"""
dict_len = int(input())
dictionary = []
while len(dictionary) < dict_len:
    word = input()
    dictionary.append(word.lower())
words_amount = int(input())
input_list = []
while len(input_list) < words_amount:
    phrase = input()
    input_list.append(phrase.split(' '))
"""
dictionary = {'champions', 'we', 'are', 'stepik'}
input_list = [['We', 'are', 'the', 'champignons'], ['We', 'are', 'the', 'Champions'], ['Stepic']]


def check_the_spell(dictionary, input_list):
    errors = set()
    for phrase in input_list:
        if len(phrase) == 1:
            phrase[0] = phrase[0].lower()
            if phrase[0] not in dictionary:
                errors.add(phrase[0])
        else:
            for word in phrase:
                word = word.lower()
                if word not in dictionary:
                    errors.add(word)
    return errors


assert check_the_spell(dictionary, input_list) == {'the', 'stepic', 'champignons'}

print('test passed')