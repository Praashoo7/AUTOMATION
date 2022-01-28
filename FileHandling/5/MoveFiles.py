import shutil
import os
from sys import *

def move(s2,d2):

    s=s2
    d=d2
    
    s1=os.path.realpath(s)+"/"

    if os.path.isdir(s):
        try:
            if os.path.isdir(d):
                os.rmdir(d)
                os.mkdir(d)
                d1=os.path.realpath(d)
            else:
                os.mkdir(d)
                d1=os.path.realpath(d)
        except Exception as c:
            print(c)
            exit()
        list=os.listdir(s)
        
        for i in list:
            try:
                shutil.move(s1+i,d1)
                print(i,"is moved from",s,"to",d)
            except Exception as c:
                print(c)
                exit()
    else:
        print("INVALID PATH")

def main():

    print("\n----MOVE FILE-----\n")
    
    if len(argv)>3 or len(argv)<2 or len(argv)==1:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : This is used to Move all Files From A Directory to Another")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : FROM_DIRECTORY_NAME TO_DIRECTORY_NAME")
        else:
            print("No such Flag Exists")
    
    if len(argv)==3:
        try:
            dfname=argv[1]
            dyname=argv[2]
            move(dfname,dyname)
        except Exception as c:
            print("\n",c)
            exit()

if __name__=="__main__":
	main()