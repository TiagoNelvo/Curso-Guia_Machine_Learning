import Voos
from Voos import *

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problema, 
                                                          schedule=mlrose.decay.GeomDecay(init_temp=10000),
                                                          random_state=0)
melhor_solucao, melhor_custo

imprimir_voos(melhor_solucao)