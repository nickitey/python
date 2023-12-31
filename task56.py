# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два
# аргумента a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам
# x из последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x,
# а элемент x является допущенным.
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и
# стандартный класс filter, но будет использовать не одну функцию, а несколько.
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент,
# и сколько не допускают. Обозначим эти количества за pos и neg.
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg,
# и возвращает True, если элемент допущен, и False иначе.

# Рассмотрим процесс допуска подробнее на следующем примере.
"""
a = [1, 2, 3]
f2(x) = x % 2 == 0 # возвращает True, если x делится на 2
f3(x) = x % 3 == 0
judge_any(pos, neg) = pos >= 1 # возвращает True, если хотя бы одна функция допускает элемент
"""
# В этом примере мы хотим отфильтровать последовательность a и оставить только те элементы, которые делятся
# на два или на три.
# Функция f2 допускает только элементы, делящиеся на два, а функция f3 допускает только элементы, делящиеся
# на три. Решающая функция допускает элемент в случае, если он был допущен хотя бы одной из функций f2 или f3,
# то есть элементы, которые делятся на два или на три.

# Возьмем первый элемент x = 1.
# f2(x) равно False, т. е. функция f2 не допускает элемент x.
# f3(x) также равно False, т. е. функция f3 также не допускает элемент x.
# В этом случае pos = 0, так как ни одна функция не допускает x, и соответственно neg = 2.
# judge_any(0, 2) равно False, значит мы не допускаем элемент x = 1.

# Возьмем второй элемент x = 2.
# f2(x) равно True
# f3(x) равно False
# pos = 1, neg = 1
# judge_any(1, 1) равно True, значит мы допускаем элемент x = 2.

# Аналогично для третьего элемента x = 3.

# Таким образом, получили последовательность допущенных элементов [2, 3].

# Класс должен обладать следующей структурой:
"""
class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
"""
# Пример использования:

"""
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]
"""

# Для наглядности я размещу функции-"правила" перед классом:


def mul2(x):  # Если эта функция возвращает True, значение pos в экземпляре класса увеличивается на один
    return x % 2 == 0  # Если нет, то увеличивается на один значение neg


# Аналогично со всеми нижеследующими функциями
def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


def mul10(x):
    return x % 10 == 0


class Multifilter:
    def judge_half(pos, neg):
        return pos >= neg
        # Функция-судья возвращает True, если половина функций-"правил" или больше вернули True

        # Здесь и далее во всех функциях-"судьях" PyCharm несмело спрашивает: а ты уверен, что первым аргументом функции
        # не должно быть self?
        # Отвечаем: уверен. Потому что функции-"судьи" - не методы класса и его экземпляров. Они работают внутри класса,
        # точнее, внутри его одного из его методов. Вызов функции-"судьи" извне в качестве метода класса или его
        # экземпляров не предполагается.
    def judge_any(aff, neg):
        return aff >= 1
        # Функция-судья возвращает True, если хотя бы одна функция-"правило" вернули True

    def judge_all(aff, neg):
        return neg == 0
        # Функция-судья возвращает True, только если ни одна функция-"правило" не вернула False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # исходная последовательность, которая будет перебираться в экземпляре класса
        self.funcs = funcs  # кортеж функций-"правил", их может быть сколько угодно
        self.judge = judge  # функция-"судья", одна из предусмотренных классом.
        # По-умолчанию: функция-"судья" пропускает элемент, если хотя бы один фильтр пройден

    def __iter__(self):  # Данная функция в классе является генератором
        for elem in self.iterable:  # в цикл принимается переданный в экземпляр класса список
            # или другой итерируемый объект
            self.aff = 0  # Первоначально планировалось, что количество "пропусков" и "недопусков" будет
            # проинициализировано нулем при создании экземпляра класса в функции init().
            self.neg = 0  # А оказалось, что это вовсе не обязательно, потому что нигде вне итератора эти переменные
            # не используются, и здесь их удобно как проинициализировать в первой итерации, так и обнулить в последующих
            for func in self.funcs:  # Для каждой функции-"правила" из кортежа funcs...
                if func(elem):  # Вызываем функцию с итерируемым элементом объекта и проверяем: если "правило"
                    # возвращает True...
                    self.aff += 1  # Увеличиваем количество "пропусков" на один.
                else:  # Если нет...
                    self.neg += 1  # увеличиваем количество "недопусков" на один.
            # Когда цикл завершил работу, все функции-"правила" вызваны с итерируемым элементов,
            # и мы проверили соответствие итерируемого элемента "правилам" фильтрации...
            if self.judge(self.aff, self.neg):  # Запускаем функцию-"судью", определенного при создании
                # экземпляра класса, и проверяем, если функция-"судья" вернула True...
                yield elem  # возвращаем этот элемент и запоминаем состояние функции-генератора.
                # В цикл на строке 130 передается следующий элемент итерируемого объекта.


a = [i for i in range(31)]  # создаем объект-список чисел от 0 до 30

assert list(Multifilter(a, mul2, mul3, mul5)) == [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24,
                                                  25, 26, 27, 28, 30]
print('Строка 152: в итоговый список вошли все элементы, которые делятся на 2, 3 и 5. При создании экземпляра класса '
      'функция-"судья" не определена, поэтому используется значение по-умолчанию: элемент "проходит" фильтр, если'
      ' удовлетворяет хотя бы одному правилу фильтрации')

assert list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)) == [0, 6, 10, 12, 15, 18, 20, 24, 30]

print('Строка 158: в итоговый список вошли элементы, которые делятся хотя бы на 2 и 3, или на 2 и 5, или на 3 и 5, '
      'при этом при создании экземпляра класса явно указана функция-"судья" и передана в качестве именованного '
      'аргумента')

assert list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)) == [0, 30]

print('Строка 164: в итоговый список вошли элементы, которые делятся одновременно на 2, 3 и 5')

assert list(Multifilter(a, mul2, mul3, mul5, mul10, judge=Multifilter.judge_all)) == [0, 30]

print('Строка 168: аналогичный результат будет, если в итоговый список включать элементы, которые делятся на 2, 3, 5 '
      'и 10')
print('Это сообщение означает, что все тесты пройдены')
