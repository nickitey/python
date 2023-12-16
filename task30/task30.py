# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно. Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст. Запишите полученный
# текст в файл и прикрепите его, как ответ на это задание. В исходном тексте не встречаются цифры, так что код
# однозначно интерпретируем. Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start
# Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со
# входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных.
# Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.

with open(r'dataset_3363_2.txt') as input_file:
    string = input_file.readline()


def decode_the_string(string):
    def multiplicate_letter(letter, multiplicator):
        return letter * multiplicator

    current_mul = ''
    current_letter = None
    result = ''
    for symbol in string:
        if symbol >= 'A' and not current_mul:
            current_letter = symbol
        elif symbol >= 'A':
            result += multiplicate_letter(current_letter, int(current_mul))
            current_mul = ''
            current_letter = symbol
        else:
            current_mul += symbol
    if current_mul:
        result += multiplicate_letter(current_letter, int(current_mul))
    return result


assert decode_the_string('a3b4c2e10b1') == 'aaabbbbcceeeeeeeeeeb'
print('All tests passed')

with open('result.txt', 'w') as res:
    res.write(decode_the_string(string))
