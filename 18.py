'''18. Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.zeros(10, dtype=int)
for i in range(10):
    A[i] = int(input(f'A[{i + 1}] = '))
print(f'Вихідний масив: {A}.\n')

prod = 1
for i in A:
    if (i < 0): # якщо зустрічаємо елемент менший нуля, перемножуємо
        prod *= i
print(f'Добуток елементів масиву, менших нуля: {prod}.') # вивід