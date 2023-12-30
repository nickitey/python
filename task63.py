import requests

# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один
# переход и из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# Sample Input 1:
# https://stepik.org/media/attachments/lesson/24472/sample0.html
# https://stepik.org/media/attachments/lesson/24472/sample2.html
# Sample Output 1:
# Yes

# Sample Input 2:
# https://stepik.org/media/attachments/lesson/24472/sample0.html
# https://stepik.org/media/attachments/lesson/24472/sample1.html
# Sample Output 2:
# No

# Sample Input 3:
# https://stepik.org/media/attachments/lesson/24472/sample1.html
# https://stepik.org/media/attachments/lesson/24472/sample2.html
# Sample Output 3:
# Yes

# url = input()
# print(f'url0 response is: {requests.get('https://stepik.org/media/attachments/lesson/24472/sample0.html').text}')
# print(f'url1 response is: {requests.get('https://stepik.org/media/attachments/lesson/24472/sample1.html').text}')
# print(f'url2 response is: {requests.get('https://stepik.org/media/attachments/lesson/24472/sample2.html').text}')


def is_in_two_hrefs(url1, url2):
    res = requests.get(url1).text.replace('stepic.org', 'stepik.org')
    res1 = requests.get(res[9:-8])
    if res1.status_code == 200:
        res1_content = res1.text.replace('stepic.org', 'stepik.org')
        if url2 in res1_content:
            return 'Yes'
        else:
            return 'No'


assert is_in_two_hrefs('https://stepik.org/media/attachments/lesson/24472/sample0.html',
                       'https://stepik.org/media/attachments/lesson/24472/sample2.html') == 'Yes'
assert is_in_two_hrefs('https://stepik.org/media/attachments/lesson/24472/sample0.html',
                       'https://stepik.org/media/attachments/lesson/24472/sample1.html') == 'No'
assert is_in_two_hrefs('https://stepik.org/media/attachments/lesson/24472/sample1.html',
                       'https://stepik.org/media/attachments/lesson/24472/sample2.html') == 'Yes'

print('I\'m here, tests passed')
