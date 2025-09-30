# stats = [
#     {
#         'movie': 'На странных берегах',
#         'bodycount': {'люди': 56, 'русалки': 2, 'ядовитые жабы': 3, 'пираты-зомби': 2}
#     },
#     {
#         'movie': 'На краю света',
#         'bodycount': {'люди': 88}
#     },
#     {
#         'movie': 'Сундук мертвеца',
#         'bodycount': {'люди': 56, 'крабы отшельники': 1}
#     },
#     {
#         'movie': 'Проклятие Черной жемчужины',
#         'bodycount': {'люди': 17}
#     },
# ]

# total_killed =0
# for element in stats:
#     total_killed += element['bodycount']['люди']
    
# print(total_killed / len(stats))

# # Вариант с list comprehention
# print(round(sum([element['bodycount']['люди'] for element in stats]) / len(stats), 0))

import numpy as np
import random

x = np.array([1,2,3])
y = np.array([4,5,6])

# Подсчёт среднего значения при помощи Numpy
print(x.mean())

print(x**y)
print(np.arange(0, 10), type(np.arange(0, 10)))
print(np.full([2,5],1))
print(np.concatenate((x,y)))
nums = np.arange(10)
print(nums)
random.shuffle(nums) # Метод сразу изменят массив, к которому он применяется
print(nums)

# Задача
n_samples = 1000
reduced_salary = np.full(n_samples, 0.5 * n_samples)
increased_salary = np.full(n_samples, 2 * n_samples)
final_salary_array = np.concatenate((reduced_salary, increased_salary))
random.shuffle(final_salary_array)
print(final_salary_array.mean())

# Для получения кол-ва строк и столбцов в массиве используется метод shape.
print(reduced_salary.shape) # Показывается только одно число потому что массив одномерный, только с одной строкой.
# Важно помнить, что в программировании если какой-то метод возвращает два значения и эти значение - кол-во строк и столбцов, то практически в 100% первое число - это число строк, а второе - число столбцов, т.е. сначала по оси Y, а потом по оси X. И в случае применения метода shape мы получаем 1000 строк с одном столбце.
print(np.full([10, 10], 1).shape) # В этом случае будет результат (10, 10), т.е. 10 строк и 10 столбцов

# Для перевода векторов в матрицы применяется метод reshape
sample = np.full([1,10], 1)
print(f"Одномерный массив с одной строкой и 10 столюцами: {sample}")
print(f"Метод reshape(2,5) делает 2 строки и 5 столбцов:\n{sample.reshape(2,5)}")
print(f"Или наоборот, reshape(5, 2) делает 5 строк и 2 столбца:\n{sample.reshape(5, 2)}")
# Если матрицу построит невозможно (3 х 3, к примеру, из 10 значений), то метод выдаст ошибку
