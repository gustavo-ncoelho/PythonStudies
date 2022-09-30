# list = used to store multiple items in a single variable

food = ["pizza", "hamburguer", "hotdog", "spaghetti"]         #lista é feita com [] e "," separando as strings

print(food[0])
print(food[1])           #aqui o número dentro da [] será o endereço da string q está na variável food
print(food[2])
print(food[3])

print("-------------------")
# FUNÇÕES NA LISTA:

food.append("ice cream")           #append adiciona uma string à lista (a última posição)
food.remove("hotdog")              #remove remove uma string da lista
food.pop()                         #pop remove a última string da lista
food.insert(0,"cake")              #insert adiciona uma string, colocando ela no endereço desejado (nesse caso, 0)
food[0] = "sushi"                  #também pode ser adicionada uma string dessa maneira, PORÉM assim irá substituir a string colocada no endereço 0 pela função insert
food.sort()                        #sort irá colocar a lista em ordem alfabética
food.clear()                       #clear irá limpar a lista


for x in food:          #aqui irá printar em sequência todas as strings da variável food
    print(x)
