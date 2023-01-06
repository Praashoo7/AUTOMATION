import time
import datetime
import schedule
import hashlib
import os
from sys import *

def FileDuplication():
    
    p=os.path.realpath("")+"\\"                    #FOLDER_NAME/FOLDER_PATH(If FolderName is gievn it finds the Folder inside current Directory and if path is Given It Goes to The Givn Path)                             
    file=""                                        #FILE_NAME

    foexists=os.path.isfile(p+file)
    
    list=[]
    list1=[]
    dict={}
    
    if foexists:
        f=p+file
        hasher=hashlib.md5()
        with open(f,"rb") as open_file:
            content=open_file.read()
            hasher.update(content)
        org=hasher.hexdigest()
    
        a=os.listdir(path=p)
        for i in a:
            f=p+i
            hasher=hashlib.md5()
            with open(f,"rb") as open_file:
                content=open_file.read()
                hasher.update(content)
            h=hasher.hexdigest()
            list.append(i)
            list1.append(h)

        for i in range(len(list)):
            dict[list[i]]=list1[i]
    
        del dict[file]

        print()
        if os.path.isfile("log.txt"):
            os.remove("log.txt")
            fc=open("log.txt","x")
            fo=open("log.txt","w")
            for i in list1:
                for keys in dict:
                    if dict[keys]==i:
                        fo.write("Name of Duplicate File is : ")
                        fo.write(keys)
                        fo.write("\n\n")
                        os.remove(p+keys)
                        print("Name of Duplicate File is Successfully Copied to log.txt and Duplicate file is removed")
                break
        else:
            fc=open("log.txt","x")
            fo=open("log.txt","w")
            for i in list1:
                for keys in dict:
                    if dict[keys]==i:
                        fo.write("Name of Duplicate File is : ")
                        fo.write(keys)
                        fo.write("\n\n")
                        os.remove(p+keys)
                        print("Name of Duplicate File is Successfully Copied to log.txt and Duplicate file is removed")
                break

    else:
        print("\nINVALID PATH/FILE")

def main():
    
    print("\n-----FILE DUPLICATION REMOVER-----\n")
    print("Scheduler Starts...")
    FileDuplication()
    schedule.every(20).seconds.do(FileDuplication)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()
