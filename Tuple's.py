#tuple = collection which is ordered and unchangeble | used to group together related data

student = ("Cabelo",22,"Homem")       #Isso é uma tuple

print(student.count("Cabelo"))        # .count para contar quantos daquela string há dentro da tuple
print(student.index("Homem"))         # .inder para mostrar o endereço da string dentro da tuple

for x in student:
    print(x)

if "Cabelo" in student:               # a condição desse if é: se a string "Cabelo" estiver dentro do tuple student, print...
    print("Cabelo is here!!!")