import gym
import random
import numpy as np
from IPython.display import clear_output
import time

start_time = time.time()

env = gym.make('Taxi-v3').env

env.render()


alpha = 0.1
gamma = 0.6
epsilon = 0.1

q_table = np.zeros([env.observation_space.n, env.action_space.n])
q_table.shape
q_table

random.uniform(0, 1)
env.action_space
np.argmax(np.array([3, 5]))



for i in range(100000):
    estado = env.reset()
    
    penalidades, recompensa = 0, 0
    done = False
    while not done:
        # Exploration
        if random.uniform(0, 1) < epsilon:
            acao = env.action_space.sample()
        # Exploitation
        else:
            acao = np.argmax(q_table[estado])
        
        proximo_estado, recompensa, done, info = env.step(acao)
        
        q_antigo = q_table[estado, acao]
        proximo_maximo = np.max(q_table[proximo_estado])
        
        q_novo = (1 - alpha)*q_antigo + alpha * (recompensa + gamma * proximo_maximo)
        q_table[estado, acao] = q_novo
        
        if recompensa ==  -10:
            penalidades += 1
        
        estado = proximo_estado
        
    if i % 100 == 0:
        clear_output(wait=True)
        print('Episódio: ', i)
    
print('Treinamento Concluido')
            
            
end_time = time.time()
print(f"Tempo de execução: {end_time - start_time} segundos")


           