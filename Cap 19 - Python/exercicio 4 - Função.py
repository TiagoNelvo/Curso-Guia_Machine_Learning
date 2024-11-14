def ler_temperatura():
    temperatura = float(input('Digite a temperatura em graus Celsius: '))
    return temperatura

def converter(temperatura_celsius):
    temperatura_f = (9 * temperatura_celsius + 160) / 5
    return temperatura_f

def mostrar(temperatura_f):
    print(temperatura_f)
    
temperatura_c = ler_temperatura()
temperatura_f = converter(temperatura_c)
mostrar(temperatura_f)