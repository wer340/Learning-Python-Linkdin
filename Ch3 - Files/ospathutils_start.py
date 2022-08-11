#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS

    print(os.name) # nt
    # Check for item existence and type
print("Item exists:",str(path.exists("wordbook.txt")))
print(f"item is file:",str(path.isfile("wordbook.txt")) )  
print(f"item is directory:",str(path.isdir("wordbook.txt")) )  
    # Work with file paths

print("###\nItem s path",path.realpath("wordbook.txt"),"\n###")    
    # Get the modification time
#ctime refers to the last metadata change for specified path in UNIX while in Windows, it refers to path creation time.
#get the time of last access of the specified path
#get the time of modification of the specified path
print("time file:",path.getctime("wordbook.txt"))
print("time file:",path.getatime("wordbook.txt"))
print("time file:",path.getmtime("wordbook.txt"))
tc=time.ctime(path.getctime("wordbook.txt"))#creation
ta=time.ctime(path.getatime("wordbook.txt"))#access
tm=time.ctime(path.getmtime("wordbook.txt"))#modify
print("time.ctime(time file c) :",tc)    
print("time.ctime(time file a) :",ta)    
print("time.ctime(time file m) :",tm)    
    # Calculate how long ago the item was modified
td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("wordbook.txt"))      
print("it has been ",td,"since the file was modified")
print("Or ,",td.total_seconds(),"seconds")  
if __name__ == "__main__":
    main()
