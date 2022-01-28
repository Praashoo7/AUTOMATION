import os

def rename(p1,ef1,et1):

    p2=p1
    p=os.path.realpath(p2)+"//"
    ef=ef1
    et=et1
	
    if os.path.isfile("log.txt"):
        os.remove("log.txt")
        fc=open("log.txt","x")
        fo=open("log.txt","w")
    else:
        fc=open("log.txt","x")
        fo=open("log.txt","w")
    
    list=[]
    v=os.listdir(p)
    if os.path.isdir(p):
        list=os.listdir(p)
        for i in list:
            if i.endswith(ef):
                e=os.path.splitext(i)[0]
                s=os.path.join(p+e+ef)
                d=os.path.join(p+e)
                os.rename(s,d+et)
                fo.write(i)
                fo.write("\n")
                print("Done")
        else:
            print("No such File with the Given Extension")

    else:
        print("File does not Exists")