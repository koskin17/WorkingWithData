# Задание 1
# Создайте numpy array с элементами от числа N до 0 (например, для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).
import numpy as np

# number = input("Введите число:")
# print(f"Numpy array от числа {number} до 0: {np.arange(int(number), -1, -1)}")

# Задание 2
# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
# number = input("Введите число:")
# diag_matrix = np.diag(np.arange(int(number), -1, -1))
# print(f"Диагональная матрица от числа {int(number)} до 0:")
# print(diag_matrix)
# print(f"Сумма диагональных элементов матрицы: {np.trace(diag_matrix)}")

# Задание 3
# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3

# first_array = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
# second_array = np.array([4, 12, -3])

# print(f"Решение системы трёх уравнений x, y, z: {np.linalg.solve(first_array, second_array)}")