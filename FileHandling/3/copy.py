import shutil
import os

def copy(s2,d2):

    s=s2
    d=d2
    
    s1=os.path.realpath(s)+"/"

    if os.path.isfile("log.txt"):
        os.remove("log.txt")
        fc=open("log.txt","x")
        fo=open("log.txt","w")
    else:
        fc=open("log.txt","x")
        fo=open("log.txt","w")

    if os.path.isdir(s):
        try:
            os.mkdir(d)
            d1=os.path.realpath(d)
        except Exception as c:
            print(c)
            exit()
        list=os.listdir(s)
        
        for i in list:
            try:
                shutil.copyfile(s1+i,d1)
                fo.write(i)
                fo.write("\n")
                print("Done")
            except Exception as c:
                print(c)
                exit()
    else:
        print("INVALID PATH")