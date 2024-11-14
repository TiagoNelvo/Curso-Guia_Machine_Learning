import gym
import random

env = gym.make('Taxi-v3').env

env.render()

#env.reset()
#env.render()


# 0 = south 1 = north 2 = east 3 = west 4 = pickup 5 = dropoff
print(env.action_space)

# 5*5*5*4 = total 
# 4 destinos
print(env.observation_space)

len(env.P)

env.P[484]

