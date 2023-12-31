#Дополнительная
#Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался. 
#Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", 
#если суммы совпадают, и "Обычный", если суммы различны.
#На вход программе подаётся строка из шести цифр.
#Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

#Sample Input 1:
#090234
#Sample Output 1:
#Счастливый

#Sample Input 2:
#123456
#Sample Output 2:
#Обычный

# put your python code here

ticket = int(input())
sixth = ticket % 10
fifth = (ticket % 100 - ticket % 10) / 10
fourth = (ticket % 1000 - ticket % 100) / 100
third = (ticket % 10000 - ticket % 1000) / 1000
second = (ticket % 100000 - ticket % 10000) / 10000
first = (ticket % 1000000 - ticket % 100000) / 100000
if first + second + third == fourth + fifth + sixth:
    print('Счастливый')
else:
    print('Обычный')