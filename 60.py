'''60. Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 3, 10)
print(f'Вихідний масив: {A}.\n')

count = 1
max = 0
for i in range(len(A)-1):
    if(A[i] == A[i+1]): # якщо наступний елемент рівний попередньому додаємо +1 до лічильника
        count += 1
        if (count > max): # якщо лічильник більший за максимальну кількість елементів підряд, то присвоюємо максимуму значення лічильника
            max = count
    else:
        count = 1 # інакше - лічильник знову скидається до одного

print(f'Найбільша кількість чисел, що йдуть підряд: {max}.')
