'''8. Створіть цілочисельний масив А [1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте
найбільший елемент масиву і його індекс.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(-15, 30, 15)
print(f'Вихідний масив: {A}.\n')
print(f'Найбільший елемент: {A.max()}.\nЙого індекс: {list(A).index(A.max())}.') # знаходимо найбільший елемент за допомогою метода max, а його індекс - за допомогою index,
                                                                                 # перетворивши при цьому масив в список