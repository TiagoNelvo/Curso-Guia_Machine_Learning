import re
#Search

frase = 'Olá, meu número de telefone é (42)0000-0000'

re.search(r'\(\d{2}\)\d{4,5}-\d{4}', frase)

frase1 = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'

re.search(r'[A-Za-z]{3}-\d{4}', frase1)

email = 'Entre em contato, meu email é teste@teste.com'

re.search(r'\w+@\w+\.com', email)

#Match

print(re.match(r'[A-Za-z]{13}-\d{4}', frase))

frase2 = 'FRT-1998 é a placa do carro'

print(re.match(r'[A-Za-z]{3}-\d{4}', frase2))

#Dindall

frase3 = 'Meu número de telfone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'

re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', frase3)

emails = ''' Nome: Teste 1
email: teste@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''

re.findall(r'\w+@\w+\.\w*', emails)
