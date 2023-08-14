import math

cateto_oposto = int(input('digite o comprimento do cateto oposto: '))
cateto_adjacente = int(input(' digite o comprimento o cateto adjacente: '))
hipotenusa = (cateto_oposto **2+cateto_adjacente**2) ** (1/2)
print(f'a hipotenusa vai medir {hipotenusa :8.2f}')

angulo = int(input("digite: "))

seno = math.sin(angulo)
cosseno = math.sin(angulo)
tangente = math.sin(angulo)

print('valor seno: {:.2} '.format(seno))
print('valor cosseno: {:.2}'.format(cosseno))
print('Valor tangente: {:.2}'.format(tangente))