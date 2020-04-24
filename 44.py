'''44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 20, 15)
print(f'Вихідний масив: {A}.\n')

sum = 0
for i in range(len(A)):
    if (i == A[i] and A[i] % 3 == 0): # перевіряємо умову
        sum += 1

print(f'Кількість елементів: {sum}.')