'''1. Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
Виконав: Лещенко В. О.'''

import numpy as np # імпортуємо numpy

arr = np.zeros(5, dtype=int) # за допомогою функції zeros створюємо масив із 5 нульових елементів цілочисельного типу
for i in range(5): # за допомогою циклу заповнюємо кожний елемент масиву з клавіатури
    arr[i] = int(input(f'A[{i + 1}] = ')) # користувач вводить поелементно

print(', '.join(map(str, arr))) # за допомогою функцій join та map вивидимо елементи через кому
print(f'Середнє арифметичне: {arr.mean()}.') # за допомогою функції mean знаходимо середнє арифметичне
