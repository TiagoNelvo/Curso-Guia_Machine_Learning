lista = []
try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))
    divisao = lista[0] / lista[1]
    
except ValueError:
    print('Erro! Valor inválido')
    
except ZeroDivisionError:
    print('Erro! Divisão por zero')
    
except IndexError: 
    print('Erro! Índice inválido')

except KeyboardInterrupt:
    print('Usuario interrompeu a execução')
    
else:
    print(f'A divisão é {divisao}')
     
 