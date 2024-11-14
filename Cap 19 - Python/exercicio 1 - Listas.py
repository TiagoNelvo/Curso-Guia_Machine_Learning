#Exercicio 1

lista = []

for _ in range(1, 6):
    valor = int(input('Digite o valor: '))
    lista.append(valor)

print(lista)

print('---------')

soma = 0
for i in range(len(lista)):
    #print(lista[i])
    soma += lista[i]
print('Soma: ', soma)

print('---------')

import numpy as np
print(np.array(lista).sum())

print('---------')