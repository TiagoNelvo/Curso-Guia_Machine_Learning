import pandas as pd
import string
import spacy
import random
import seaborn as sns
import numpy as np

# Etapa 1: Importação e instalação das bibliotecas

from google.colab import drive
drive.mount('/content/drive')

#Etapa 2: Carregamento da base de dados

base_dados = pd.read_csv('/content/base_treinamento.txt', encoding = 'utf-8')

base_dados.shape

base_dados.head()

base_dados.tail()

sns.countplot(y='emocao', data=base_dados, label = 'Contagem');

# Etapa 3: Função para pré-processamento dos textos

pontuacoes = string.punctuation
pontuacoes

from spacy.lang.pt.stop_words import STOP_WORDS
stop_words = STOP_WORDS

print(stop_words)

len(stop_words)

#pln = spacy.load('pt')
pln = spacy.load("pt_core_news_sm")

pln

def preprocessamento(texto):
    texto = texto.lower()
    documento = pln(texto)

    lista = []
    for token in documento:
        #lista.append(token.text)
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pontuacoes]
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  return lista

teste = preprocessamento('Estou aPrendendo 1 10 23 processamento de linguagem natural, Curso em Curitiba')
teste







