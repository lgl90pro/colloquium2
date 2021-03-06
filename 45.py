'''45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
Виконав: Лещенко В. О.'''

import numpy as np
from math import sqrt

R = float(input('Введіть радіус даху: ')) # користувач вводить радіус півкола
length = np.array([], dtype=int)
delta_x = R / 5
x = 0

while (x < 2 * R - delta_x):
    x += delta_x
    h = sqrt(x*(2 * R - x)) # знаходимо довжину опори за формулою
    length = np.append(length, h) # додаємо кожний раз довжину опори в масив

print(f'\nМасив з довжин опор:{np.round(length,2)}') # виведемо довжини, округли до 2 знаків після коми
