import os
from sys import *

def df1(n1):

    n=n1
    p=os.path.realpath(n)+"\\"
    
    list=os.listdir(p)
    if os.path.exists(p):
        for i in list:
            s=os.path.getsize(p+i)
            if s>1000000:
                print("\n",i,"(Size=",s,")""is removed")
                os.remove(p+i)
            else:
                print("\n",i,"(Size=",s,")""is not Greater that 1MB and is not Removed")
    else:
        print("No such Directory")
        
def main():

    print("\n----DELETE FILE-----\n")
    
    if len(argv)>2 or len(argv)<1 or len(argv)==1:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : Deletes all Files from the Given Folder Which are Greater than 1MB in Size.")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : DIRECTORY_NAME")
        else:
            print("No such Flag Exists")
    
    if len(argv)==2:
        try:
            dname=argv[1]
            df1(dname)
        except Exception as c:
            print("\n",c)
            exit()

if __name__=="__main__":
	main()
