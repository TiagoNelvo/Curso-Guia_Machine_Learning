import Criação_Mapa

grafo = Grafo()

grafo.arad.mostra_adjacentes()
print('------')
grafo.zerind.mostra_adjacentes()

vetor = VetorOrdenado(5)
vetor.insere(grafo.arad)
vetor.insere(grafo.craiova)
vetor.insere(grafo.bucharest)
vetor.insere(grafo.dobreta)

print('------')

vetor.imprime()
