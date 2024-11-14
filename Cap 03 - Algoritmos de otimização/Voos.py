#Representação do Problema

#lista
pessoas = [('Lisboa','LIS'),
           ('Madrid','MAD'),
           ('Paris','CDG'),
           ('Dublin','DUB'),
           ('Bruxelas','BRU'),
           ('Londres','LHR')]

pessoas[5]

destino = 'FCO'

#dicionario
'''voos = {('BRU','FCO'): ['15:44','18:55', 382]}

voos

voos[('BRU', 'FCO')][0], voos[('BRU', 'FCO')][1], voos[('BRU', 'FCO')][2]
'''

voos = {}
for linha in open(r'C:\Users\Tilto\Desktop\Work\Guia IA e ML\Cap 03 - Algoritmos de otimização\flights.txt'):
    #print(linha)
    #print(linha.split(','))
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida,chegada, int(preco)))
    
voos

voos[('LIS', 'FCO')]

voos [('FCO', 'LIS')]

agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]
#len(agenda)

def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas [i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                    volta[0], volta[1], volta[2]))        
        
    print('Preço total: ', total_preco)
    
imprimir_voos(agenda)

# Fitness Function

def fitness_function(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
    return total_preco

# fitness_function(agenda)


import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

fitness = mlrose.CustomFitness(fitness_function)

problema = mlrose.DiscreteOpt(length=12, fitness_fn=fitness,
                              maximize = False, max_val=10)


# Hill Climb
melhor_solucao, melhor_custo = mlrose.hill_climb(problema, random_state=1)
melhor_solucao, melhor_custo

print('Hill Climb')
imprimir_voos(melhor_solucao)
print('-----------')

voos[('BRU', 'FCO')]

# Simulated Annealing

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, 
                                                          schedule=mlrose.decay.GeomDecay(init_temp=10000),
                                                          random_state=1)
melhor_solucao, melhor_custo

print('Simulated Annealing')
imprimir_voos(melhor_solucao)
print('-----------')

# Algoritmo Genético

melhor_solucao, melhor_custo = mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2, random_state=1)
melhor_solucao, melhor_custo

print('Algoritmo Genético')
imprimir_voos(melhor_solucao)
print('-----------')