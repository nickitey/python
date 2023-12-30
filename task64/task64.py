# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
# с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
import csv


def get_most_regular_crime(crimestat):
    i = 0
    for row in crimestat:
        for i in range(len(row)):
            if row[i] == 'Primary Type':
                break
        break
    crimes_amount = {}
    for row in crimestat:
        if row[i] in crimes_amount:
            crimes_amount[row[i]] += 1
        else:
            crimes_amount[row[i]] = 1
    biggest_count = 0
    most_popular_crime = ''
    for crime in crimes_amount:
        if crimes_amount[crime] > biggest_count:
            most_popular_crime = crime
            biggest_count = crimes_amount[crime]
    return most_popular_crime


with open(r'crimes.csv') as crimes:
    crime_stats = csv.reader(crimes)
    assert get_most_regular_crime(crime_stats) == 'THEFT'

print('You\'re goddamn right (c) Mr. Heisenberg from Breaking Bad')
