import os
import datetime
import pandas as pd
import smtplib
import schedule
import time
import random
from email.message import EmailMessage
import re
import urllib.request

def send():
    
    date=datetime.datetime.now()
    m=date.month
    d=date.day
    dict={}
    dict1={}
    dict2={}
    sendlist=[]
    dcal=[]
    mcal=[]
    
    qlist=["May all the joy you have spread around come back to you a hundredfold. Happy birthday.","May you receive the greatest of joys and everlasting bliss. You are a gift yourself, and you deserve the best of everything. Happy birthday.","Be happy, for today; you were born to bring blessings and inspiration to all. Happy birthday!","Here is a wish for your birthday. May you receive whatever you ask for, may you find whatever you seek. Happy birthday.","Hope all your birthday wishes come true."]
    alist=["b1.jpg","b2.jpg","b3,jpg","b4.jpg","b5.jpg"]
    
    dates=pd.read_excel("birth1.xlsx")

    monthlist=dates["Month"].tolist()
    namelist=dates["Name"].tolist()
    datelist=dates["Date"].tolist()
    maillist=dates["Email"].tolist()
    
    for i in range(len(maillist)):
        dict[maillist[i]]=datelist[i]
        
    for i in range(len(maillist)):
        dict1[maillist[i]]=monthlist[i]
        
    for i in range(len(maillist)):
        dict2[maillist[i]]=namelist[i]
        
    for keys in dict:
        if dict[keys]==d:
            dcal.append(keys)
    
    for keys in dict1:
        if dict1[keys]==m:
            mcal.append(keys)
            
    for i in dcal:
        for j in mcal:
            if i==j:
                sendlist.append(i)

    regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    for i in sendlist:
        if re.fullmatch(regex,i):
            pass
        else:
            sendlist.remove(i)
            print("\nWARNING :",i,"is an Invalid Email Address and is Removed")
    

    print("\nList of Email-ID's who have Birthdays Today :",sendlist,"\n")
    
    if len(sendlist)==0:
        print("No Birthdays Today.")
        quit()

    for i in dict2:
        for j in sendlist:
            if i==j:
                contacts = [keys]
                msg = EmailMessage()
                msg['Subject'] = 'HAPPY BIRTHDAY!'
                msg['From'] = "example@gmail.com"
                msg['To'] = j
                msg.set_content('Happy Birthday '+dict2[i]+'\n\n'+random.choice(qlist))
                
                msg.add_attachment(b"test",maintype="jpg",subtype="png", filename=random.choice(alist))
                
                try:
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login("example@gmail.com", "******")
                        smtp.send_message(msg)
                except Exception as e:
                    print("Username and Password not accepted\nError :",e)
                    quit()
                    
                print("Mail Sent to",dict2[i],"at",j)
    
def main():

    #schedule.every().day.at("00:00").do(send)
    
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

    try:
        urllib.request.urlopen("http://google.com",timeout=3)
    except Exception as c:
        print("\nInternet Connection Required.\nERROR :",c)
        quit()

    try:
        send()
    except Exception as c:
        print(c)

if __name__=="__main__":
	main()
