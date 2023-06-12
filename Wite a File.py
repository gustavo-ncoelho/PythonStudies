
text = "Hello world\nArquivo criado no python\nHehehehe"

with open('test1.txt', 'w') as file:    #O 'w' diz que o arquivo vai ser escrito, se for 'r', é lido
    file.write(text)                    

text2 = "\nOla mundo\nXesque do Bresque"

with open('test1.txt', 'a') as file:        #Se for 'a' é append, ou seja, será adicionado a frase ao arquivo
    file.write(text2)