import time
import datetime
import schedule
import hashlib
import os
from sys import *

def FileDuplication(p1,file1):
    
    p=p1                                    
    file=file1   

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
        
        print(dict)
        print(org)
        print()

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
    if (len(argv)>3) or (len(argv)<2):
        print("INVALID ARGUMENT")
        print("Use -u Flag for Usage")
        print("Use -h Flag for Help")
        quit()
    
    if len(argv)==2:
        if argv[1]=="-h" or argv[1]=="-H":
            print("HELP : FOLDER_PATH FILE_NAME")
        elif argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : Used to Delete Duplications of a File.")
        else:
            print("There is no Such Flag")
            quit()
        
    if len(argv)==3:
        try:
            folderpath=argv[1]
            filename=argv[2]
            FileDuplication(folderpath,filename)
        except Exception as c:
            print(c)
            quit()
    
if __name__=="__main__":
    main()
