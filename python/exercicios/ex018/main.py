import math

n1 = int(input('Digite um ângulo: '))

cos = math.cos(math.radians(n1))
sin = math.sin(math.radians(n1))
tg = math.tan(math.radians(n1))

print(f'O ângulo {n1} tem o seno {sin}, o cosseno {cos} e a tangente {tg}')