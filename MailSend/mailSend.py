import os
import datetime
import pandas as pd
import smtplib
import schedule
import time

def send():
    
    date=datetime.datetime.now()
    y=date.year
    m=date.month
    d=date.day
    dict={}
    list=[]
    sendmail=[]
    
    try:
        dates=pd.read_excel("birth.xlsx")
    except Exception:
        print("\nFile Not Present")
        exit()
    
    yearlist=dates["Year"].tolist()
    monthlist=dates["Month"].tolist()
    
    datelist=dates["Date"].tolist()
    maillist=dates["Email"].tolist()
    
    for i in range(len(maillist)):
        dict[maillist[i]]=datelist[i]
    
    for i in monthlist:
        if m==i:
            for keys in dict:
                if dict[keys]==d:
                    sendmail.append(keys)
            server=smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("example@gmail.com", "******")
            message="Happy Birthday"
            server.sendmail("example@gmail.com", sendmail, message)
            print("\nDone")
            server.quit()
            break
    
def main():

    schedule.every().day.at("00:00").do(send)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__=="__main__":
	main()
