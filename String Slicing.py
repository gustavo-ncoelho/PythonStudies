# slicing = create a substring by extracting elements from another string

#            INDEX []      SLICE ()

#      [start:stop:step]   OBS: O START É INCLUSIVO E O START É EXCLUSIVO
name = "Gustavo Coelho"
                               #O 0 pode ser subtituído por nenhum caracter
first_name = name[0:7]         #name[0:7] irá mostrar somente do caracter 0 ao 7 da string name
last_name = name[8:14]         #mesma coisa aqui, porém como o stop é exclusivo, coloca-se sempre um caracter a mais no stop
funky_name = name[0:14:3]      #O step irá mostrar os caracteres de forma alternada (se for 1 mostrará todos, 2 mostrará um sim um não, 3 mostrará 1 sim dois não...)
reversed_name = name[::-1]     #-1 no step irá mostrar a string ao contrário

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# SLICE function:           Igual a função anterior, porém é uma função que irá ser criada e se tornará uma "variável"

website = "http://google.com"
website2 = "http://wikipedia.com"

slice1 = slice(7,-4)     #Quando se vai cortar a string no start usa-se o caracter inicial e no stop usa-se o caracter final porém contando de trás para frente, portanto é utilizado o sinal de negativo (pois se conta de trás para frente)

print(website[slice1])   #Aqui foi utilizada a função slice que foi criada na linha 22, aplicada na variável website
print(website2[slice1])      #Mesma função slice só que em outra variável




