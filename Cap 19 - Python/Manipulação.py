with open('frase1.txt') as tex:
    for linha in tex:
        print(linha)
         
#with open('frase1.txt') as tex:
    #r = tex.readlines()
    
    
with open('texto2.txt', 'w') as texto:
    texto.write('Olá a todos')