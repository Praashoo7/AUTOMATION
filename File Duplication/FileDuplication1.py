import time
import datetime
import schedule
import hashlib
import os
from sys import *

c=0

def FileDuplication():
    
    global c
    p="D:/Python C/MinProj/AUTOMATION/Check/"
    file="Demo.txt"

    list=[]
    list1=[]
    dict={}
    
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
    for keys in dict:
        if org==dict[keys]:
            print(keys,"was a Duplication of Data and is Deleted")
            os.remove(p+keys)

    c=c+1
    if c==3:
        exit()

def main():
    
    print("Scheduler Starts...")
    FileDuplication()
    schedule.every(20).seconds.do(FileDuplication)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
    main()