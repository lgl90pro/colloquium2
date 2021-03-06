'''25. Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(10, 100, 10)
print(f'Вихідний масив: {A}.\n')

prod = 1
for i in A:
    if (i % 5 == 0): # перевіряємо на кратність 5 і перемножуємо
        prod *= i

if (prod != 1):
    print(f'Добуток елементів, що задовільняють умові: {prod}.')
else:
    print('Немає чисел, що задовільняють умові.')