'''15. Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(100, 200, 20)
print(f'Вихідний масив: {A}.\n')

sum = 0
for i in A:
    if (i % 2 == 0): # якщо остача від ділення дає 0 - елемент парний
        sum += i # додаємо його до суми

print(f'Сума парних елементів: {sum}.') # вивід