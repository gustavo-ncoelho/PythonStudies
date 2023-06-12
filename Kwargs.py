
def hello(**names):                       #Quando se usa "**", o argumenta se tornará um dicionário
    print("Hello", end=" ")               # Usa-se o loop para ir printando os valores colocados
    for key,value in names.items():
        print(value, end=" ")

hello(tittle="Sr.", first="Cabelera", middle="Nervoso", last="da Silva")   #A chave de cada valor é adicionado quando se chama a função