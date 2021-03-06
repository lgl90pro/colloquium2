'''35. Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 20, 10)
print(f'Вихідний масив: {A}.\n')

for i in range(len(A) - 1):
    if (A[i] > A[i+1]): # якщо наступний елемент менший за попередній, пропускаємо
        pass
    else: # інакше - масив не упорядкований по спаданню, виводимо і припиняємо роботу програми
        print('Масив не є упорядкованим по спаданню.')
        exit(0)

print('Масив є упорядкованим по спаданню.') # якщо програма ще працює, то гілка else не виконалась, і масив упорядкований
