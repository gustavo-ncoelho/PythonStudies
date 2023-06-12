name = "gustavo coelho"

if(name[0].islower()): 
    name = name.capitalize()  #capitalize coloca a primeira letra em maiusculo

print(name)

print("-------------------------")

first_name = name[:7].upper()   #":7" seleciona a string do algarismo 0 até o 7
last_name = name[8:].capitalize()   #aqui é selecionado do 8 até o fim da string

print(first_name)
print(last_name)

print("-------------------------")

name2 = "gustavo coelho!"

last_character = name2[-1]      #quado se usa negativo, o index é contado de traz pra frente, logo -1 é o ultimo algarismo

print(last_character)