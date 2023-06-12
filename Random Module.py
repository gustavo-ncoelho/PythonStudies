import random

x = random.randint(1,6)     #randint entrega números aleatoriamente dentro do range estipulado nos ()
y = random.random()         #gera números aleatórios entre 0 e 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)               #Aqui será escolhido algum item da lista aleatoriamente

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)                        #Aqui é "embaralhado" os valores de uma lista

print(x)
print(y)
print(z)
print(cards)