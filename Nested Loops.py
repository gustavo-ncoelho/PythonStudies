 #  Nested loops = "Loops Aninhados"  =  Um loop dentro do outro
 #  Pode-se usar esta função para desenhar um retângulo de símbolos, como mostra o exemplo:

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")       #o end="" fará com que o print encerre após a satisfação das condições
    print()                         #Esse print é para fechar o loop de fora