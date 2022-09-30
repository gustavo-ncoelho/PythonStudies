# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}         # quando o grupo de dados está dentro de {}, isso é um set,
dishes = {"bowl","plate","cup"}             # set's não são ordenados e os seus dados não tem endereço fixo

for x in utensils:               # Nesse caso, os itens sempre serão printados de forma aleatória pois
    print(x)                     # não tem endereço nem ordem

print("___________________")

# Operações com set's:

utensils.add("napkin")                       #adiciona um dado
utensils.remove("fork")                      #remove um dado
utensils.clear()                             #limpa o set
utensils.update(dishes)                      #adiciona um set para outro (não definitivo)
dinner_table = utensils.union(dishes)        #une dois set's, nesse caso foi feita outra variável com a junção das duas set's

for x in dinner_table:
    print(x)

print(dishes.difference(utensils))           #mostra a diferença entre sets (qual string tem em utensils que não tem em dishes)
print(utensils.intersection(dishes))         #mostra a interseção entre sets (quais strings tem em comum)


