'''23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(150, 300, 20)
print(f'Вихідний масив: {A}.\n')

sum = 0
for i in A:
    if (i < A.mean()): # перевіряємо, чи число менше середнього арифметичного і додаємо
        sum += i

print(f'Сума елементів, що задовільняють умові: {sum}.')
