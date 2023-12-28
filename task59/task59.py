# Вам дана в архиве [ссылка](https://stepik.org/media/attachments/lesson/24465/main.zip)
# файловая структура, состоящая из директорий и файлов.
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".
# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных
# в лексикографическом порядке.
import os

result = []
for current_dir in os.walk('./'):

    for files in current_dir:
        for file in files:
            if file[-3:] == '.py':
                print(str(current_dir[0])[2:])
                result.append(str(current_dir[0])[2:])
                break
result.sort()

with open(r'C:\Users\Никита\Desktop\python\task59\result.txt', 'w') as output:
    output.write('\n'.join(result))
