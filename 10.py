'''10. Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(-15, 5, 10)
print(f'Температура за декаду листопада: {A}.\n')
sum = 0
for i in A:
    if (i < -10): # якщо знахожимо температуру нижче -10 градусів, добавляємо до лічильника
        sum += 1

print(f'Температура опускалась нижче -10 градусів {sum} раз(и/ів).') # вивід