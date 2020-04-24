'''46. Задана таблиця назв товарів, що випускаються заводом. Визначте, чи
повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть
назву першого товару з таблиці.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.array(['Хліб', 'Молоко', 'Цукор', 'Масло', 'Олія', 'Спеції', 'Йогурт', 'Хліб'])
print(f'Вихідний масив: {A}.\n')

for i in range(len(A) - 1):
    if (A[0] == A[i + 1]): # якщо повторюється, то видаляємо за допомогою зрізу
        A = A[1:len(A)]
        break # припиняємо цикл

print(f'Після перевірки: {A}.')
