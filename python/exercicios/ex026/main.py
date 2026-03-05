f = input('Digite uma frase: ')

s = f.strip()

m = s.upper()
a = m.count('A')
p = m.find('A')
u = m.rfind('A')

print(f'A letra "a" apareceu {a} vezes, sendo na primeira vez na posição {p+1} e a ultima vez na posição {u+1}')