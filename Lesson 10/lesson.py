# # Задача 1 из Lesson 10\pyda-lab-0420.ipynb

# string_01 = "History is always written by the winners. hen two cultures clash, the loser is obliterated, and the winner writes the history books-books which glorify their own cause and disparage the conquered foe. As Napoleon once said, 'What is history, but a fable agreed upon?"

# print(f"Полная длина строки, включая пробелы: {len(string_01)}")

# print(f"Длина строки без пробелов (способ с replace: len(string_01.replace(' ', ''))): {len(string_01.replace(' ', ''))}")
# print(f"Длина строки без пробелов (способ с count: len(string_01) - string_01.count(' ')): {len(string_01) - string_01.count(' ')}")

# list_from_string_01 = string_01.split()
# print(f"Количество слов во все строке (через преобразование строки в список и подсчёт длины списка): {len(list_from_string_01)}")

# import re

# def words_with_symbol(symbol, string):
#     clear_string = re.sub(r'[^\w\s]', '', string) # Очистка строки от всех символов, которые не буквы
#     count = 0
#     for word in clear_string.split(' '):
#         word = word.lower()
#         if word.startswith(symbol):
#             count += 1
#             print(word)        
        
#     return count

# letter = 'w'
# print(f"Количество слов, начинающихся с буквы {letter}: {words_with_symbol(letter, string_01)}")


# Задача 2
# import random

# Вариант 1
# number = ''
# while '3' not in number:
#     number = ''.join([str(random.randint(0, 9)) for i in range(6)]) # Пока 3 не будет в числе цикл будет формировать число из 6 знаков

# print(number)

# Вариант 2 (нормальный)
# random_number = list(''.join(random.choices('0124567890', k=5)) + '3')
# random.shuffle(random_number)
# print(''.join(random_number), type(''.join(random_number)))


# Задача 3
# Вариант 1
# list_01 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
# sum_of_elements_1 = 0
# sum_of_elements_2 = 0
# for element in list_01:
#     if element > 10 and element < 100:
#         sum_of_elements_1 += element
    
#     if element > 200 and element < 500:
#         sum_of_elements_2 += element
        
# print(sum_of_elements_1)
# print(sum_of_elements_2)

# Вариант 2: с list comprehention
# print(sum([x for x in list_01 if 10 < x < 100 or 200 < x < 500]))


# Задача 4
# students = [
#     ["0001", "Антонов", "Антон", "Игоревич", "20.08.2009","БСТ161"],
#     ["1102", "Богов", "Артем", "Игоревич", "25.01.2010","БСТ162"],
#     ["0333", "Глаголева", "Анастасия", "Николаевна", "11.07.2009", "БСТ163"],
#     ["4004", "Степанова", "Наталья", "Александровна", "13.02.2008", "БСТ161"],
#     ["0045", "Боков", "Игорь", "Харитонович", "02.06.2009", "БСТ161"],
#     ["0096", "Васильков", "Валентин", "Сергеевич", "20.03.2009", "БСТ164"],
#     ["0607", "Сиропова", "Виолетта", "Эдуардовна", "28.05.2010", "БСТ162"]
# ]

# students_dict = {s[0]:s[1:] for s in students}
# print(students_dict)

# def group_change(student_id, new_group):
#     students_dict[student_id][4] = new_group 
#     print(f"Группа для студента {student_id} успешно изменена на {new_group}")
#     return new_group

# students_in_group = []

# def all_students_in_group(group):
#     for value in students_dict.values():
#         if value[4] == group:
#             students_in_group.append([value[0], value[1], value[2]])
            
#     return students_in_group
            
# print(all_students_in_group("БСТ161"))

# Задача 5
matrix = [ 
    [0,1,2,4,8], 
    [6,2,2,1,9], 
    [3,3,3,3,3], 
    [4,6,7,1,2], 
    [5,7,3,4,0] 
]

# Решение с Numpy
# import numpy

# print(numpy.sum(matrix)) # Numpy позволяет в одну строку сразу посчитать сумму всей матрицы

total_sum = 0
for element in matrix:
    total_sum += sum(element)
    
print(total_sum)

# Вычисление максимума из сумм списков в матрице
# В Numpy у sum() есть необязательный аргумент - ось, которая сообщает по какой оси в матрице выполнять суммирование. Если передать 0, то суммирование будет происходить по столбцам матрицы, т.е. как будто списки написаны друг над другом и будут суммироваться цифры из образовавшихся столбцов
import numpy

print(max(numpy.sum(matrix, axis=0)))

# В этом решении я суммировал цифры в каждом списке
max = sum(matrix[0])
for element in matrix:
    if max < sum(element):
        max = sum(element)
        
print(max)