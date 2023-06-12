
def add(*args):                      #Para colocar um número ilimitado de argumentos, coloca-se o "*" antes
    sum = 0                          # do nome dos argumentos   
    for x in args:                   # AQUI o args vira uma tuple
        sum = sum + x
    return sum

print(add(1,2,3,4,5,6))

print("---------------------------")

def somar(*numeros):
    soma = 0
    numeros = list(numeros)         #nessa linha transforma-se numeros de tuple para lista, para poder alterar algum valor
    numeros[0] = 0                  # no caso o numero de index 0 será igual a 0
    for x in numeros:
        soma += x
    return soma

print(somar(1,2,3,4,5,6))