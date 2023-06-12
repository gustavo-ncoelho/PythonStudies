import os

path = "C:\\Users\\Gustavo\\Desktop\\Arquivos"

if os.path.exists(path):                 #Par saber se a localização existe ou não
    print("That location exists!!!")
    if os.path.isfile(path):            # Para saber se é arquivo ou não
        print("Thats a file")
    elif os.path.isdir(path):           # Para saber se é pasta ou não
        print("Thats a directory")
else:
    print("That location doesn't exist!!!")