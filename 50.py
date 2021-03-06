'''50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
Виконав: Лещенко В. О.'''

import numpy as np

A = np.random.randint(0, 100, 10) # виграшні квитки

N = int(input('Введіть N: ')) # користувач вводить номер
if (N in A): # якщо номер є у виграшних - виводимо це
    print('\nКвиток виграшний!')
else: # інакше - виводимо що немає
    print('\nКвиток не виграшний.')

print(f'Номери виграшних квитків: {A}.')