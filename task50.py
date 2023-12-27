# Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным
# способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.

# Рассмотрим класс Loggable:
import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


# У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
# добавляя при этом текущее время.
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении
# элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного
# элемента.

# Примечание
# Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он будет
# содержать метод log, описанный выше.


class LoggableList(list, Loggable):
    def append(self, elem):
        super(LoggableList, self).append(elem)
        super(LoggableList, self).log(elem)


class LoggableList2(Loggable, list): # Я не понимаю, почему, но вот так тоже вполне работает.
    def __init__(self):
        self.lst = []

    def append(self, elem):
        self.lst.append(elem)
        return super(LoggableList2, self).log(elem)


y = LoggableList()
y.append('Hi!') # Wed Dec 27 19:56:09 2023: Hi!
y.append('See you soon!') # Wed Dec 27 19:56:09 2023: See you soon!

z = LoggableList2()
z.append('Hello!') # Wed Dec 27 19:56:09 2023: Hello!
z.append('Good bye!') # Wed Dec 27 19:56:09 2023: Good bye!
