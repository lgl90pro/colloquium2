'''4. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Виконав: Лещенко В. О.'''

import numpy as np

surname = np.array(['Трофімов', 'Сидоренко', 'Іванов', 'Карпенко', 'Демчук'])
letter = input('Введіть букву: ') # користувач вводить букву
for i in surname:
    if (i[0] == letter or i[0] == letter.upper()): # якщо перша буква прізвища = введеній малій або великій літера, виводимо прізвище
        print(i)