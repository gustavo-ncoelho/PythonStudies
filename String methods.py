name = "cabelera"
number = "28213493"

print(len(name))                 #Comando len(lenght) mostra qual o tamanho da string e caracteres
print(len(number))
print(name.find("l"))            #Comando find mostra aonde está o caracter indicado dentro da string
print(name.capitalize())         #Comando capitalize coloca a string com a inicial maiúscula
print(name.upper())              #Comando upper coloca toda string em maiúsculo
print(name.lower())              #Comando lower coloca toda string em minúsculo
print(name.isdigit())            #isdigit vai retornar se a string é composta de números ou não
print(number.isalpha())          #isalpha vai retornar se a string é composta por letras do alfabeto
print(number.count("3"))         #Comando count vai contar quantos do caracter tem na string
print(name.replace("a","u"))     #replace irá substituir o primeiro caracter pelo segundo
print(name*3)                    #multiplica a string