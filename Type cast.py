#type casting = converter o tipo de dado de uma variável para outro

x = 1     #int
y = 2.0   #float
z = "3"   #str

print(float(x))          #float(x) transforma x em float
print(str(y))            #str(y) transforma y em string
print(int(z)*3)          #int(z) transforma z em int, logo pode fazer operações (antes não podia pois era str)

    #Para mudar a variável permanentemente deve-se igualar ela à conversão:

x = float(x)
y = int(y)
z = str(z)