# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.

# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# aba_baba
# ab_aba_ba
# abab_aba

# Sample Input 1:
# abababa
# aba
# Sample Output 1:
# 3

# Sample Input 2:
# abababa
# abc
# Sample Output 2:
# 0

# Sample Input 3:
# abc
# abc
# Sample Output 3:
# 1

# Sample Input 4:
# aaaaa
# a
# Sample Output 4:
# 5


def get_count_with_overlaps(str, substr):
    count = 0
    for i in range(len(str)):
        if str.startswith(substr, i) > 0:
            count += 1
    return count


assert get_count_with_overlaps('abababa', 'aba') == 3
assert get_count_with_overlaps('abababa', 'abc') == 0
assert get_count_with_overlaps('abc', 'abc') == 1
assert get_count_with_overlaps('aaaaa', 'a') == 5

print('I\'m ok, I\'m not alcoholic (c) Little Big')
