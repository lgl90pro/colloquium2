'''3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
Виконав: Лещенко В. О.'''

import numpy as np

surname = np.array(['Трофімов', 'Сидоренко', 'Іванов', 'Карпенко', 'Демчук']) # за допомогою array створюємо масив із прізвищ
for i in surname[::-1]: # за допомогою зрізу виводимо з останнього
    print(i)