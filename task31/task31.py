# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
# смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
# частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
# вывести лексикографически первое (можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3

with open(r'dataset_3363_3.txt') as input_file:
    experimental_string = ''
    for line in input_file:
        experimental_string += line.strip()


def get_most_popular(string):
    def sort_words(same_string):
        sorted_list = [i.lower() for i in same_string.split(' ')]
        return sorted(sorted_list, reverse=True)

    # Нам же никто не запрещал пользоваться результатами собственной интеллектуальной деятельности?
    def count_words(word_list):  # Из таска 28
        result = {}
        for word in word_list:
            word = word.lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
        return result

    sorted_words_list = sort_words(string)
    dict_of_string = count_words(sorted_words_list)
    biggest_count = 0
    most_popular = ''
    for key in dict_of_string:
        if dict_of_string[key] >= biggest_count:
            biggest_count = dict_of_string[key]
            most_popular = key
    return most_popular + ' ' + str(biggest_count)


assert get_most_popular('abc a bCd bC AbC BC BCD bcd ABC') == 'abc 3'
assert get_most_popular(experimental_string) == 'bxacd 11'

# Последний тест: на входе в функцию данный мне платформой файл, содержимое которого я заранее не знал, на выходе -
# то, что у меня приняли в качестве ответа
print('tests are done')
