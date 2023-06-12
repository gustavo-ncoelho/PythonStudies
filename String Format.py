
animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)        #maneira convencional de concatenar
print("The {} jumped over the {}".format(animal, item))    #usando o .format pode-se colocar as variáreis detro de placeholders, no caso os {}
print("The {1} jumped over the {0}".format(animal, item))  # Pode-se também usar números para indicar o index da variável q se quer utilizar de dentro do format()
print("The {lua} jumped over the {lua}".format(vaca="cow", lua="moon"))  #Aqui não é necessário criar uma variável, pode-se usar palavra chave

text = "The {} jumped over the {}"
print(text.format(animal,item))           #pode-se usar o .fomat para uma varíavel que é uma string e possui placeholders

print("-------------------------")

name = "Cabelo"

print("Hello, my name is {}, nice to meet you".format(name))
print("Hello, my name is {:12}, nice to meet you".format(name))     #Aqui pode-se alocar casas dentro da string para a variável
print("Hello, my name is {:<12}, nice to meet you".format(name))    # Aqui é a mesma coisa da linha de cima
print("Hello, my name is {:>12}, nice to meet you".format(name))    # Os espaços alocados vem antes da variável
print("Hello, my name is {:^12}, nice to meet you".format(name))    # A variável é centralizada nos espaços

print("FORMATAÇÃO EM NÚMEROS:")

number1 = 3.14459
number2 = 10000

print("The number pi is {:.2f}".format(number1))    #Aqui é escolhido qntas casas decimais se quer mostrar
print("The number is {:,}".format(number2))         #Aqui transforma o número em decimal
print("The number is {:b}".format(number2))         #Aqui transforma o numero em binário
print("The number is {:o}".format(number2))         #Aqui transforma o numero em octadecimal
print("The number is {:x}".format(number2))         #Aqui transforma o numero em hexadecimal minúsculo
print("The number is {:X}".format(number2))         #Aqui transforma o numero em hexadecimal Maiúsculo
print("The number is {:e}".format(number2))         #Aqui transforma o numero em notação científica
