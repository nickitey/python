# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:

# y больше или равно x
# y делится нацело на 5

def closest_mod_5(x):
    y = x
    while y % 5 != 0:
        y += 1
    return y


assert closest_mod_5(7) == 10
assert closest_mod_5(11) == 15
assert closest_mod_5(97) == 100
assert closest_mod_5(105) == 105
assert closest_mod_5(19398177912838267736571639287636) == 19398177912838267736571639287640

print('all tests passed')


def also_closest_mod_5(x): # Это уже тяга к извращениям просто проснулась
    for i in range(x, 2 ** 300): # С любовью вспомнил JS с его числом Infinity
        if i % 5 != 0:
            i += 1
        else:
            return i


assert also_closest_mod_5(7) == 10
assert also_closest_mod_5(11) == 15
assert also_closest_mod_5(97) == 100
assert also_closest_mod_5(105) == 105
assert also_closest_mod_5(19398177912838267736571639287636) == 19398177912838267736571639287640

print('These tests also passed')