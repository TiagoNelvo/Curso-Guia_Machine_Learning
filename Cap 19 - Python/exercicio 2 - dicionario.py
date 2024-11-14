print('------------------------------------')

#Exercicio 2

alunos = {}
for _ in range(1, 4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota
print(alunos)
print('------------------------------------')
print(alunos['Pedro'])
print('------------------------------------')
print(alunos.values())
print('------------------------------------')

soma = 0
for nota in alunos.values():
    #print(nota)
    soma += nota
print('Média: ', soma / 3)
print('------------------------------------')