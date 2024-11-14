#import numpy as np

def soma (a, b):
    return a + b

#soma(float(input('Digite o primeiro numero: ')), float(input('Digite o segundo numero: ')))

r = soma(3,2)
print(r)



def calcula_energia_potencial_gravitacional(m, h, g = 10 ):
    '''
    Calcula a energia potencial gravitacional 
    Argumentos:
    m: massa, entrada como variável float
    h: altura, entrada como uma variável float
    
    Argumento opcional:
    g: aceleração gravitacional, com valor default de 10 
    '''
    e = g * m * h
    return e

calcula_energia_potencial_gravitacional(30, 12)

calcula_energia_potencial_gravitacional(30, 12, 9.8)