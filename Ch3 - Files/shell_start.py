#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("wordbook.txt"):
        # get the path to the file in the current directory
        src=path.realpath("wordbook.txt")
        # let's make a backup copy by appending "bak" to the name
        # dst=src+".bak"
        # shutil.copy(src,dst)
        # rename the original file
        # os.rename("wordbook.txt","wordbookPlus.txt")
        # now put things into a ZIP archive
        # root_dir ,tail=path.split(src)
        # print("root dir :",root_dir,"\n tail : ",tail)
        # shutil.make_archive("backup","zip",root_dir)
        # more fine-grained control over ZIP files
        with ZipFile("backupPlus.zip","w",compresslevel=2) as file_zip:
            file_zip.write("rosa1.jpg")
            file_zip.write("rosa2.jpg")

      
if __name__ == "__main__":
    main()
