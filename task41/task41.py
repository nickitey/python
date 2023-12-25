# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepik.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.
import requests

with open(r'dataset_3378_3.txt') as input_file:
    url = input_file.readline().strip()

response = requests.get(url)
while response.text.split()[0] != 'We':
    response = requests.get(f'https://stepik.org/media/attachments/course67/3.6.3/{response.text}')

print(response.text)
