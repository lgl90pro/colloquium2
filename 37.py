'''37. Розсортуйте заданий лінійний масив по зростанню.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 20, 10)
print(f'Вихідний масив: {A}.\n')

A.sort() # сортуємо за допомогою метода sort
print(f'Відсортований масив: {A}.')