# 1. Перевести содержимое файла purchase_log.txt в словарь
# 2. Для каждого user_id из файла visit_log.csv определить категорию, если покупка была.
# 3. В файл funnel.csv записать визиты из файла visits_log.csv, в которых были покупки с указанием категории.

import json

# Task 1
with open('Lesson 6\purchase_log.txt', 'r', encoding='utf-8') as purchase:
    with open('dict_purchase.txt', 'a', encoding='utf-8') as dict_purchase:
        for line in purchase:
            line = line.strip()
            dict_purchase.write(line)
            
json_file = json.loads('dict_purchase.txt')
# Task 2
# visits = open('Lesson 6/visit_log.csv', 'r', encoding='utf-8')
# for i in range(9):
#     print(visits.readline())
        