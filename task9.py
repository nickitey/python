#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки 
#сначала максимальное, потом минимальное, после чего оставшееся число.
#На ввод могут подаваться и повторяющиеся числа.

#Sample Input 1:
#8
#2
#14
#Sample Output 1:
#14
#2
#8

#Sample Input 2:
#23
#23
#21
#Sample Output 2:
#23
#21
#23

# put your python code here

a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
    if b >= c:
        print(c)
        print(b)
    else:
        print(b)
        print(c)
elif b >= a and b >= c:
    print(b)
    if a >= c:
        print(c)
        print(a)
    else: 
        print(a)
        print(c)
elif c >= a and c >= b:
    print(c)
    if a >= b:
        print(b)
        print(a)
    else: 
        print(a)
        print(b)