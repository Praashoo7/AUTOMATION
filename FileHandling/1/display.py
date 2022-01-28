import os

def display(p1,f1):

    list=[]
    list1=[]
    dict={}
    p2=p1
    p=os.path.realpath(p2)+"//"
    f=f1

    if os.path.isfile("log.txt"):
        os.remove("log.txt")
        fc=open("log.txt","x")
        fo=open("log.txt","w")
    else:
        fc=open("log.txt","x")
        fo=open("log.txt","w")
    
    if os.path.isdir(p)==True:
        list=os.listdir(p)
        for i in list:
            if i.endswith(f):
                fo.write(i)
                fo.write("\n")
                print("Done")
        else:
            print("No Such File with the Given Extension")
    
    else:
        print("No Such Directory Exists")