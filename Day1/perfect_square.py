# Accepet a number from user and check whether it  is perfect square or not

import math as m

input_num = int(input('Enter a number: '))
sqrt_num = m.sqrt(input_num)
f_num = m.floor(sqrt_num)
print('NUM is a PS' if (input_num == f_num * f_num) else 'NUM is not a PS')