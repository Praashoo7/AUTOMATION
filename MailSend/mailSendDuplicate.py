import os
import sys
import hashlib
from datetime import datetime
from email.message import EmailMessage
import schedule
import smtplib
import time

def mailS(f,f2,st1,tf1,tdf1,m):
    
    starttime=str(st1)
    totalfiles=str(tf1)
    totaldfiles=str(tdf1)
    attach=f
    name=f2
    rm=m
    
    with open(attach,"rb") as d:
        file_data=d.read()
    
    if len(file_data)==0:
    
        msg = EmailMessage()
        msg['Subject'] = "Log_File("+f2+")"
        msg['From'] = "example@gmail.com"
        msg['To'] = rm
        msg.set_content("Log File contains names of Duplicate Files Removed per Time Interval.\n\nStarting Time of Scanning : "+starttime+"\nTotal Files Scanned : "+totalfiles+"\nTotal Duplicate Files : "+totaldfiles+"\n\nNo Duplications Found.")
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("example@gmail.com", "******")
            smtp.send_message(msg)
        print("\nMail Sent")
    
    else:
    
        msg = EmailMessage()
        msg['Subject'] = "Log_File("+f2+")"
        msg['From'] = "example@gmail.com"
        msg['To'] = rm
        msg.set_content("Log File contains names of Duplicate Files Removed per Time Interval.\n\nStarting Time of Scanning : "+starttime+"\nTotal Files Scanned : "+totalfiles+"\nTotal Duplicate Files : "+totaldfiles)
    
        msg.add_attachment(file_data,maintype="text",subtype="file_type", filename=name)
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("example@gmail.com", "******")
            smtp.send_message(msg)
        print("\nMail Sent")
    
def fd():
    
    d=""                                     #DIRECTORY_NAME_TO_FIND_DUPLICATIONS
    mail=""                                  #RECEIVER E-MAIL_ID

    p=os.path.realpath(d)+"\\"
    
    list=[]
    list1=[]
    list2=[]
    dict={}
    
    dt=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fn=str("log("+dt+").txt")

    if os.path.isdir(""):                   #DIRECTORY_NAME_TO_BE_CREATED_TO_STORE_LOG_FILE
        fp=os.path.join("",fn)              #PATH_OF_THE_DIRECTORY_TO_BE_CREATED_TO_STORE_LOG_FILE
        fc=open(fp,"x")
        fw=open(fp,"w")
    else:
        os.mkdir("")                        #DIRECTORY_NAME_TO_BE_CREATED_TO_STORE_LOG_FILE
        fp=os.path.join("",fn)              #PATH_OF_THE_DIRECTORY_TO_BE_CREATED_TO_STORE_LOG_FILE
        fc=open(fp,"x")
        fw=open(fp,"w")

    if os.path.isdir(d):
        listf=os.listdir(d)
        for i in listf:
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

        i=0
        for j in dict:
            if dict[j] not in list2:
                list2.append(dict[j])
            else:
                fw.write("File Name : ")
                fw.write(j)
                i=i+1
                fw.write("\n")
                os.remove(p+j)
        fw.close()
    print("\nFile Written.")
    mailS(fp,fn,dt,len(listf),i,mail)

def main():
    
    schedule.every(60).minutes.do(fd)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
	main()