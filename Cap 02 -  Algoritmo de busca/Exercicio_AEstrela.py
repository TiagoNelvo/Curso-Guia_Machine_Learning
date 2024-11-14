import numpy as np

# Grafo
class Vertice:
    
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
        
    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)
        
    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class Grafo:
    def __init__(self):
        self.portoUniao = Vertice("Porto União", 203)
        self.pauloFrontin = Vertice("Paulo Frontin", 172)
        self.canoinhas = Vertice("Canoinhas", 141)
        self.irati = Vertice("Irati", 139)
        self.palmeira = Vertice("Palmeira", 59)
        self.campoLargo = Vertice("Campo Largo", 27)
        self.curitiba = Vertice("Curitiba", 0)
        self.balsaNova = Vertice("Balsa Nova", 41)
        self.araucaria = Vertice("Araucaria", 23)
        self.saoJose = Vertice("São José dos Pinhais", 13)
        self.contenda = Vertice("Contenda", 39)
        self.mafra = Vertice("Mafra", 94)
        self.tijucas = Vertice("Tijucas do Sul", 56)
        self.lapa = Vertice("Lapa", 74)
        self.saoMateus = Vertice("São Mateus do Sul", 123)
        self.tresBarras = Vertice("Três Barras", 131)

        self.portoUniao.adiciona_adjacente(Adjacente(self.pauloFrontin, 46))
        self.portoUniao.adiciona_adjacente(Adjacente(self.canoinhas, 78))
        self.portoUniao.adiciona_adjacente(Adjacente(self.saoMateus, 87))

        self.pauloFrontin.adiciona_adjacente(Adjacente(self.portoUniao, 46))
        self.pauloFrontin.adiciona_adjacente(Adjacente(self.irati, 75))

        self.canoinhas.adiciona_adjacente(Adjacente(self.portoUniao, 78))
        self.canoinhas.adiciona_adjacente(Adjacente(self.tresBarras, 12))
        self.canoinhas.adiciona_adjacente(Adjacente(self.mafra, 66))

        self.irati.adiciona_adjacente(Adjacente(self.pauloFrontin, 75))
        self.irati.adiciona_adjacente(Adjacente(self.palmeira, 75))
        self.irati.adiciona_adjacente(Adjacente(self.saoMateus, 57))

        self.palmeira.adiciona_adjacente(Adjacente(self.irati, 75))
        self.palmeira.adiciona_adjacente(Adjacente(self.saoMateus, 77))
        self.palmeira.adiciona_adjacente(Adjacente(self.campoLargo, 55))

        self.campoLargo.adiciona_adjacente(Adjacente(self.palmeira, 55))
        self.campoLargo.adiciona_adjacente(Adjacente(self.balsaNova, 22))
        self.campoLargo.adiciona_adjacente(Adjacente(self.curitiba, 29))

        self.curitiba.adiciona_adjacente(Adjacente(self.campoLargo, 29))
        self.curitiba.adiciona_adjacente(Adjacente(self.balsaNova, 51))
        self.curitiba.adiciona_adjacente(Adjacente(self.araucaria, 37))
        self.curitiba.adiciona_adjacente(Adjacente(self.saoJose, 15))

        self.balsaNova.adiciona_adjacente(Adjacente(self.curitiba, 51))
        self.balsaNova.adiciona_adjacente(Adjacente(self.campoLargo, 22))
        self.balsaNova.adiciona_adjacente(Adjacente(self.contenda, 19))

        self.araucaria.adiciona_adjacente(Adjacente(self.curitiba, 37))
        self.araucaria.adiciona_adjacente(Adjacente(self.contenda, 18))

        self.saoJose.adiciona_adjacente(Adjacente(self.curitiba, 15))
        self.saoJose.adiciona_adjacente(Adjacente(self.tijucas, 49))

        self.contenda.adiciona_adjacente(Adjacente(self.balsaNova, 19))
        self.contenda.adiciona_adjacente(Adjacente(self.araucaria, 18))
        self.contenda.adiciona_adjacente(Adjacente(self.lapa, 26))

        self.mafra.adiciona_adjacente(Adjacente(self.tijucas, 99))
        self.mafra.adiciona_adjacente(Adjacente(self.lapa, 57))
        self.mafra.adiciona_adjacente(Adjacente(self.canoinhas, 66))

        self.tijucas.adiciona_adjacente(Adjacente(self.mafra, 99))
        self.tijucas.adiciona_adjacente(Adjacente(self.saoJose, 49))

        self.lapa.adiciona_adjacente(Adjacente(self.contenda, 26))
        self.lapa.adiciona_adjacente(Adjacente(self.saoMateus, 60))
        self.lapa.adiciona_adjacente(Adjacente(self.mafra, 57))

        self.saoMateus.adiciona_adjacente(Adjacente(self.palmeira, 77))
        self.saoMateus.adiciona_adjacente(Adjacente(self.irati, 57))
        self.saoMateus.adiciona_adjacente(Adjacente(self.lapa, 60))
        self.saoMateus.adiciona_adjacente(Adjacente(self.tresBarras, 43))
        self.saoMateus.adiciona_adjacente(Adjacente(self.portoUniao, 87))

        self.tresBarras.adiciona_adjacente(Adjacente(self.saoMateus, 43))
        self.tresBarras.adiciona_adjacente(Adjacente(self.canoinhas, 12))

grafo = Grafo()

# Vetor Ordenado
class VetorOrdenado:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)
        
#  Referência para o vértice e comparação com a distância para o objetivo       

    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        if self.ultima_posicao == -1:
            posicao = 0
        else:
            for i in range(self.ultima_posicao + 1):
                posicao = i
                if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                    break
                if i == self.ultima_posicao:
                    posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1
        
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', 
                      self.valores[i].vertice.rotulo, ' - ', 
                      self.valores[i].vertice.distancia_objetivo, ' - ', 
                      self.valores[i].custo, ' - ', 
                      self.valores[i].distancia_aestrela)

# Algoritmo A*

class AEstrela:
    
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False
        
    def buscar(self, atual):
        print('------------')
        print(f'Atual: {atual.rotulo}')
        atual.visitado = True
        
        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()
            
            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0].vertice)

# Execução
busca_aestrela = AEstrela(grafo.curitiba)
busca_aestrela.buscar(grafo.portoUniao)
