
from genericpath import isdir
import os
from os import path


src=path.realpath("")
print(src)

try :
    path.isdir(src+'/result')
    path_dir=path.join(src,"result")
    make_dir=os.mkdir(path_dir)


except:
    pass

dir_list=os.listdir(src)
total_size=0
for file in dir_list:
    with open("./result/brief.txt","a+") as note:
            note.write(file+"\n")
    src_file=path.realpath(file)
    total_size+= path.getsize(src_file)
    
with open("./result/brief.txt","a+") as note:
    note.write("\n-----------------------------------------------------------\n"+"TOTAL SIZE :"+str(total_size)+"\n")

