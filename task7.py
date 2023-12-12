#Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, 
#после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#Обратите внимание, что на вход программе приходят вещественные числа.

#Sample Input 1:
#5.0
#0.0
#mod
#Sample Output 1:
#Деление на 0!

#Sample Input 2:
#-12.0
#-8.0
#*
#Sample Output 2:
#96.0

#Sample Input 3:
#5.0
#10.0
#/
#Sample Output 3:
#0.5

# put your python code here

a = float(input())
b = float(input())
action = input()

if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '/':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a / b)
elif action == '*':
    print(a * b)
elif action == 'mod':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a % b)
elif action == 'pow':
    print(a ** b)
elif action == 'div':
    if b == 0:
        print('Деление на 0!')
    else:
        print(a // b)