import os
from sys import *

def dlf(n1):

    n=n1
    p=os.path.realpath(n)+"\\"
    
    list1=[]
    list=os.listdir(p)
    dict={}
    if os.path.exists(p):
        
        for i in list:
            s=os.path.getsize(p+i)
            list1.append(s)
        
        for i in range(len(list)):
            dict[list[i]]=list1[i]
        
        for keys in dict:
            m=max(list1)
            if dict[keys]==m:
                os.remove(p+keys)
                print("\n",keys,"was the largest file and is Deleted")
    else:
        print("No such Directory")
        
def main():

    print("\n----DELETE LARGEST FILE-----\n")
    if len(argv)>2 or len(argv)<1 or len(argv)==1:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : Deletes the Largest File from the Given Folder.")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : DIRECTORY_NAME")
        else:
            print("No such Flag Exists")
    
    if len(argv)==2:
        try:
            dname=argv[1]
            dlf(dname)
        except Exception as c:
            print("\n",c)
            exit()

if __name__=="__main__":
	main()