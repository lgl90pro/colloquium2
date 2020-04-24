'''42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Виконав: Лещенко В. О.'''

import numpy as np
from math import factorial

A = np.random.randint(0, 30, 15)
print(f'Вихідний масив: {A}.\n')

sum = 0
for i in range(len(A)):
    if (i**2 < A[i] < factorial(i)): # переріємо умову, якщо істинна - +1 до лічильника
        sum += 1

print(f'Кількість елементів, що задовільняють умові: {sum}.')