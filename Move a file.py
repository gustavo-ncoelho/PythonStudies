import os

source = "move.txt"
destination = "C:\\Users\\Gustavo\\Desktop\\Arquivos\\move.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)   #src, destination
        print(source + " whas moved")
except FileNotFoundError:
    print(source + " was not found")

source2 = "folder"
destination2 = "C:\\Users\\Gustavo\\Desktop\\Arquivos\\folder"

try:
    if os.path.exists(destination2):
        print("There is already a folder there")
    else:
        os.replace(source2, destination2)   #src, destination
        print(source2 + " whas moved")
except FileNotFoundError:
    print(source2 + " was not found")