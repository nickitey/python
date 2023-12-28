# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

# Пример входного файла:
# ab
# c
# dde
# ff

# Пример выходного файла:
# ff
# dde
# c
# ab


with open(r'dataset_24465_4.txt', 'r') as input:
    input_raw = input
    input_text = []
    for line in input_raw:
        input_text.insert(0, line)

with open(r'result.txt', 'w') as output:
    for line in input_text:
        output.write(line)
