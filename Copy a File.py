# copyfile() = copies content of a file
# copy() =     copyfile() + permission mode + destination can be a directiory
# copy2() =    copy() + copies metadata(file's creation and modification times)

import shutil

shutil.copyfile('test1.txt', 'copy.txt')  #src,dst  (source, destination)

shutil.copyfile('test1.txt', 'C:\\Users\\Gustavo\\Desktop\\Arquivos\\Copy.txt')