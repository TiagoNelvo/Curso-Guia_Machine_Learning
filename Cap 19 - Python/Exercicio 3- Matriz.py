#Exercicio 3
import numpy as np


print('------------------------------------')

matriz = np.array([[3,4,1],[3,1,5]])

print(matriz)

print('------------------------------------')

matriz.shape

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
print('Soma: ', soma)
print('------------------------------------')