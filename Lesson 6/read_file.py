# f = open('visit_log.csv', 'r', encoding='utf-8')

# def read_file(file):
#     f = open(file, 'r', encoding='utf-8')
#     for i in range(5):
#         print(f.readline())
        
#     f.close()
        
# read_file('visit_log.csv')

# Задание: отфильтровать один файл по условию (наличие context) и отфильтрованные результаты написать в другой файл.
# with open ('visit_log.csv', 'r') as f_log:
#     with open ('visits_context.csv', 'w') as f_context:
#         for line in f_log:
#             if 'context' in line:
#                 f_context.write(line)

# В чтении файлов хорошо помогает json.loads
# import json

# i = 0
# with open('purchase_log.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         line = line.strip()
        
#         line_to_json = json.loads(line)
#         print(line_to_json, type(dict))
        
#         i += 1
#         if i > 5:
#             break

# Для сохранения всего объекта в файл используется модуль pickle. Он очень хорошо помогат есть надо, к примеру, сохранить большую модель с большим кол-вом зависимостей и/или результатов, которые считались длительное время. Таким образом можно всю модель сохранить в файл по результатам работы, а потом при необходимости эту модель просто загрузить в переменную и всё.

# Чтение всех файлов и папок
import os

for file in os.listdir('data'):
    print(file)
    
# Для чтения всех файлов и папок, в том числе вложенных
for root, directory, file in os.walk('data'):
    print(root, directory, file) 