alunos = {'Pedro': 8.0,'Maria': 10.0, 'Amilton': 7.5}
alunos

with open('alunos.txt', 'w') as arquivo:
    for aluno, nota in alunos.items():
        arquivo.write(f'{aluno}, {nota}\n')
        
with open('alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)