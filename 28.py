'''28. Знайти кількість парних елементів одновимірного масиву.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 200, 15)
print(f'Вихідний масив: {A}.\n')

sum = 0
for i in A:
    if (i % 2 == 0): # якщо остача від ділення на два - нуль, то елемент парний
        sum += 1

if (sum != 0):
    print(f'Кількість парних елементів масиву: {sum}.')
else:
    print('Парних елементів у масиві немає.')