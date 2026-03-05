v = float(input('Digite o valor em metros:'))

km = v/1000
hm = v/100
dam = v/10
dm = v*10
cm = v*100
mm = v*1000

print(f'O valor de {v}m em centímetros é {cm}cm e o valor em milímetros é {mm}mm')

print(f'KM = {km}\nHM = {hm}\nDAM = {dam}\nDM = {dm}\nCM = {cm}\nMM = {mm}')