#for loop = irá repetir o for pedido uma quantidade X de vezes
#              for loop = limitado
#              while loop = infinito

for i in range(10):           #Essa função irá printar a variável i de 0 a 9 (10 vezes), lembrando que range é a função de "alcance" e sempre irá mostrar cada caracter um por um
    print(i+1)                #Para contar de 1 a 10, adiciona-se o + 1 (pois a contagem sempre começa do 0


for y in range(50,100):       #Aqui será mostrado de 50 a 99 (Pois o stop é exclusivo). LEMBRANDO QUE
    print(y)                  #    (star,stop,step)


for x in "Gustavo Coelho":    #Aqui cada linha irá mostrar um caractere da string, até o final da string
   print(x)

# PARA FAZER UMA CONTAGEM REGRESSIVA DEVE-SE IMPORTAR A FUNÇÃO "TIME"

import time                         #O correto é sempre importar no início do cógio

for seconds in range(10,0,-1):       #Contar de 10 à 0 usando o step -1. LEMBRANDO QUE (start,stop,step)
    print(seconds)                   #second aqui é somente uma variável
    time.sleep(1)                    #time.sleep(1) é o que diz que deve-se mostrar os números a cada 1 segundo
print("Happy new year!")











