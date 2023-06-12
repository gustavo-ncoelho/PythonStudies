import os
import shutil

path = "test2.txt"
folder = "remove"
tree = "tree_folder"

try:
    os.remove(path)        #deleta somente arquivos
    os.rmdir(folder)       #deleta somente pastas VAZIAS
    shutil.rmtree(tree)    #deleta pastas com conteúdo dentro
except PermissionError:
    print("You don't have permission to delete that")
except FileNotFoundError:
    print("That file was not found")
else:
    print("file/folder was removed")
