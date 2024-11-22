from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.aid import AID
from sys import argv

class Agent(Agent):
    def __init__(self, aid):
        super(Agent, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Ola')
        
if __name__ == '__main__':
    numero_agentes = 2
    c = 0
    agentes = list()
    for i in range(numero_agentes):
        porta = int(argv[1]) + c
        nome_agente = 'agente{}@localhost:{}'.format(porta, porta)
        agente = Agente(AID(name=nome_agente))
        agentes.append(agente)
        c += 1000
    start_loop(agentes)

# Executar no prompt
# pade start-runtime --port 20000 agente1.py


