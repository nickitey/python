# Дополнительная В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
# они говорили каким-то странным набором звуков. В какой-то момент один из биологов раскрыл секрет информатиков: они
# использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий
# ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: Напишите программу, которая умеет
# шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего
# идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
# Получаем следующие строки, которые и передаём на вывод программы: *d*%*d*#*d* dacabac

# Sample Input 1:
# abcd
# *d%#
# abacabadaba
# *%*d*%
# Sample Output 1:
# *d*%*d*#*d*
# dacabac

# Sample Input 2:
# dcba
# badc
# dcba
# badc
# Sample Output 2:
# badc
# dcba


"""
word = input()
input_list = [word]
while len(input_list) < 4:
    word = input()
    input_list.append(word)
"""


def encode_or_decode(dictionary, word):
    result = ''
    for symbol in word:
        result += dictionary[symbol]
    return result


def encode_and_decode(input_list):
    encode_dict = {}
    decode_dict = {}
    for i in range(len(input_list[0])):
        encode_dict[input_list[0][i]] = input_list[1][i]
        decode_dict[input_list[1][i]] = input_list[0][i]
    return [encode_or_decode(encode_dict, input_list[2]), encode_or_decode(decode_dict, input_list[3])]


assert encode_and_decode(['abcd', '*d%#', 'abacabadaba', '#*%*d*%']) == ['*d*%*d*#*d*', 'dacabac']
assert encode_and_decode(['dcba', 'badc', 'dcba', 'badc']) == ['badc', 'dcba']

print('all tests passed')
