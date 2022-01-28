import shutil
import os

def copyex(s2,d2,e2):

    s=s2
    d=d2
    e=e2
    
    s1=os.path.realpath(s)+"//"

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
            if i.endswith(e):
                f=os.path.splitext(i)[0]
                s2=os.path.join(s1+f+e)
                shutil.copy(s2,d1)
                fo.write(i)
                fo.write("\n")
                print("Done")
        else:
            print("No Such file Exists with the Given Extension")
    else:
        print("No such Directory Exists")