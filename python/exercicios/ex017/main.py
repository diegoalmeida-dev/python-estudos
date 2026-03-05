'''from math import sqrt

a1 = float(input('Digite o ângulo do cateto oposto: '))
a2 = float(input('Digite o ângilo do cateto adjascente: '))

h = sqrt(a1**2 + a2**2)
print(f'A hipotenusa é {h} !')'''

import math

a1 = float(input('Digite o ângulo do cateto oposto: '))
a2 = float(input('Digite o ângilo do cateto adjascente: '))

h = math.hypot(a1, a2)

print(f'A hipotenusa é {h} !')
