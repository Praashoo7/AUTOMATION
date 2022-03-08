import os
import datetime
import pandas as pd
import smtplib
from email.message import EmailMessage
import schedule
import time
import re
import random
import urllib.request

def dmycalculateCModule(pyear):   

    d=datetime.datetime.now()
    year=d.year
    month=d.month
    date=d.day
    cdays1=0
    cdays2=0
    
    try:
        byear=pyear
        bmonth=month
        bdate=date
    except Exception:
        print("\nINVALID INPUT")
        quit()
    
    if (byear>d.year) and (bmonth>d.month) and (bdate>d.date):
        print("Invalid Data")
        exit()
    elif (byear==year) and (bmonth==month) and (bdate>date):
        print("Invalid Data")
        exit()
    elif bmonth<=0:
        print("Invalid Month")
        exit()
    elif bmonth>12:
        print("Invalid Month")
        exit()
    elif byear<=0:
        print("Invalid Year")
        exit()
    elif byear>2021:
        print("Invalid Year")
        exit()
    elif bdate<=0:
        print("Invalid Date")
        exit()
    elif bdate>31:
        print("Invalid Date")
        exit()

    cyear=year-byear
    
    if bmonth==12:
        cmonth=cyear*12
    else:
        #for i in range(12,0,-1):
        cmonth=(cyear*12)+month-bmonth
    
    Jan=31
    Fab=28
    Mar=31
    Apr=30
    May=31
    Jun=30
    Jul=31
    Aug=31
    Sep=30
    Oct=31
    Nov=30
    Dec=31
    
    if month>bmonth:
        cdays1=cyear*365
        
        if bmonth==2:
            Rd=28-bdate
        elif bmonth==(4 or 6 or 9 or 11):
            Rd=30-bdate
        else:
            Rd=31-bdate
    
        if month-bmonth==1 and month==1:
            cdays2=Rd+date
        elif month-bmonth==1 and month==2:
            cdays2=Rd+date
        elif month-bmonth==1 and month==3:
            cdays2=Rd+date
        elif month-bmonth==1 and month==4:
            cdays2=Rd+date
        elif month-bmonth==1 and month==5:
            cdays2=Rd+date
        elif month-bmonth==1 and month==6:
            cdays2=Rd+date
        elif month-bmonth==1 and month==7:
            cdays2=Rd+date
        elif month-bmonth==1 and month==8:
            cdays2=Rd+date
        elif month-bmonth==1 and month==9:
            cdays2=Rd+date
        elif month-bmonth==1 and month==10:
            cdays2=Rd+date
        elif month-bmonth==1 and month==11:
            cdays2=Rd+date
        elif month-bmonth==1 and month==12:
            cdays2=Rd+date
        elif bmonth==1 and month==3:
            cdays2=Rd+Fab+date
        elif bmonth==1 and month==4:
            cdays2=Rd+Fab+Mar+date
        elif bmonth==1 and month==5:
            cdays2=Rd+Fab+Mar+Apr+date
        elif bmonth==1 and month==6:
            cdays2=Rd+Fab+Mar+Apr+May+date
        elif bmonth==1 and month==7:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+date
        elif bmonth==1 and month==8:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+date
        elif bmonth==1 and month==9:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+date
        elif bmonth==1 and month==10:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+date
        elif bmonth==1 and month==11:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif bmonth==1 and month==12:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==2 and month==4:
            cdays2=Rd+Mar+date
        elif bmonth==2 and month==5:
            cdays2=Rd+Mar+Apr+date
        elif bmonth==2 and month==6:
            cdays2=Rd+Mar+Apr+May+date
        elif bmonth==2 and month==7:
            cdays2=Rd+Mar+Apr+May+Jun+date
        elif bmonth==2 and month==8:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+date
        elif bmonth==2 and month==9:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+date
        elif bmonth==2 and month==10:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+date
        elif bmonth==2 and month==11:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif bmonth==2 and month==12:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==3 and month==5:
            cdays2=Rd+Apr+date
        elif bmonth==3 and month==6:
            cdays2=Rd+Apr+May+date
        elif bmonth==3 and month==7:
            cdays2=Rd+Apr+May+Jun+date
        elif bmonth==3 and month==8:
            cdays2=Rd+Apr+May+Jun+Jul+date
        elif bmonth==3 and month==9:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+date
        elif bmonth==3 and month==10:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+date
        elif bmonth==3 and month==11:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif bmonth==3 and month==12:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==4 and month==6:
            cdays2=Rd+May+date
        elif bmonth==4 and month==7:
            cdays2=Rd+May+Jun+date
        elif bmonth==4 and month==8:
            cdays2=Rd+May+Jun+Jul+date
        elif bmonth==4 and month==9:
            cdays2=Rd+May+Jun+Jul+Aug+date
        elif bmonth==4 and month==10:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+date
        elif bmonth==4 and month==11:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+Oct+date
        elif bmonth==4 and month==12:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==5 and month==7:
            cdays2=Rd+Jun+date
        elif bmonth==5 and month==8:
            cdays2=Rd+Jun+date
        elif bmonth==5 and month==9:
            cdays2=Rd+Jun+July+Aug+date
        elif bmonth==5 and month==10:
            cdays2=Rd+Jun+July+Aug+Sep+date
        elif bmonth==5 and month==11:
            cdays2=Rd+Jun+Jul+Aug+Sep+Oct+date
        elif bmonth==5 and month==12:
            cdays2=Rd+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==6 and month==8:
            cdays2=Rd+Jul+date
        elif bmonth==6 and month==9:
            cdays2=Rd+Jul+Aug+date
        elif bmonth==6 and month==10:
            cdays2=Rd+Jul+Aug+Sep+date
        elif bmonth==6 and month==11:
            cdays2=Rd+Jul+Aug+Sep+Oct+date
        elif bmonth==6 and month==12:
            cdays2=Rd+Jul+Aug+Sep+Oct+Nov+date
        elif bmonth==7 and month==9:
            cdays2=Rd+Aug+date
        elif bmonth==7 and month==10:
            cdays2=Rd+Aug+Sep+date
        elif bmonth==7 and month==11:
            cdays2=Rd+Aug+Sep+Oct+date
        elif bmonth==7 and month==12:
            cdays2=Rd+Aug+Sep+Oct+Nov+date
        elif bmonth==8 and month==10:
            cdays2=Rd+Sep+date
        elif bmonth==8 and month==11:
            cdays2=Rd+Sep+Oct+date
        elif bmonth==8 and month==12:
            cdays2=Rd+Sep+Oct+Nov+date
        elif bmonth==9 and month==11:
            cdays2=Rd+Oct+date
        elif bmonth==9 and month==12:
            cdays2=Rd+Oct+Nov+date
        elif bmonth==10 and month==12:
            cdays2=Rd+Nov+date
        elif bmonth==3 and month==1:
            cdays2=Rd+Fab+bdate
        elif bmonth==4 and month==1:
            cdays2=Rd+Fab+Mar+bdate
        elif bmonth==4 and month==2:
            cdays2=Rd+Mar+bdate
        elif bmonth==5 and month==1:
            cdays2=Rd+Fab+Mar+Apr+bdate
        elif bmonth==5 and month==2:
            cdays2=Rd+Mar+Apr+bdate
        elif bmonth==5 and month==3:
            cdays2=Rd+Apr+bdate
        elif bmonth==6 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+bdate
        elif bmonth==6 and month==2:
            cdays2=Rd+Mar+Apr+May+bdate
        elif bmonth==6 and month==3:
            cdays2=Rd+Apr+May+bdate
        elif bmonth==6 and month==4:
            cdays2=Rd+May+bdate
        elif bmonth==7 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+bdate
        elif bmonth==7 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+bdate
        elif bmonth==7 and month==3:
            cdays2=Rd+Apr+May+Jun+bdate
        elif bmonth==7 and month==4:
            cdays2=Rd+May+Jun+bdate
        elif bmonth==7 and month==5:
            cdays2=Rd+Jun+bdate
        elif bmonth==8 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+bdate
        elif bmonth==8 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+bdate
        elif bmonth==8 and month==3:
            cdays2=Rd+Apr+May+Jun+Jul+bdate
        elif bmonth==8 and month==4:
            cdays2=Rd+May+Jun+Jul+bdate
        elif bmonth==8 and month==5:
            cdays2=Rd+Jun+Jul+bdate
        elif bmonth==8 and month==6:
            cdays2=Rd+Jul+bdate
        elif bmonth==9 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+bdate
        elif bmonth==9 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+bdate
        elif bmonth==9 and month==3:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+bdate
        elif bmonth==9 and month==4:
            cdays2=Rd+May+Jun+Jul+Aug+bdate
        elif bmonth==9 and month==5:
            cdays2=Rd+Jun+Jul+Aug+bdate
        elif bmonth==9 and month==6:
            cdays2=Rd+Jul+Aug+bdate
        elif bmonth==9 and month==7:
            cdays2=Rd+Aug+bdate
        elif bmonth==10 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==3:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==4:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==5:
            cdays2=Rd+Jun+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==6:
            cdays2=Rd+Jul+Aug+Sep+bdate
        elif bmonth==10 and month==7:
            cdays2=Rd+Aug+Sep+bdate
        elif bmonth==10 and month==8:
            cdays2=Rd+Sep+bdate
        elif bmonth==11 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==3:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==4:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==5:
            cdays2=Rd+Jun+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==6:
            cdays2=Rd+Jul+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==7:
            cdays2=Rd+Aug+Sep+Oct+bdate
        elif bmonth==11 and month==8:
            cdays2=Rd+Sep+Oct+bdate
        elif bmonth==11 and month==9:
            cdays2=Rd+Oct+bdate
        elif bmonth==12 and month==1:
            cdays2=Rd+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==2:
            cdays2=Rd+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==3:
            cdays2=Rd+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==4:
            cdays2=Rd+May+Jun+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==5:
            cdays2=Rd+Jun+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==6:
            cdays2=Rd+Jul+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==7:
            cdays2=Rd+Aug+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==8:
            cdays2=Rd+Sep+Oct+Nov+bdate
        elif bmonth==12 and month==9:
            cdays2=Rd+Oct+Nov+bdate
        elif bmonth==12 and month==10:
            cdays2=Rd+Nov+bdate
        
        ld=int(cyear/4)
        
        cdays=cdays1+cdays2+ld
        cweeks=cdays/7
        yy=float(cdays/365)
    
        print("")
        print("You have been wasting Oxygen for : \n")
    
        print(yy," Years,")
        print(cmonth," Months,")
        print(cweeks," Weeks and")
        print(cdays," Days")
    
    if month<bmonth:
        
        cdays1=(cyear-1)*365
        cyear1=cyear-1
        
        if bmonth==2:
            Rd1=28-bdate
        elif bmonth==(4 or 6 or 9 or 11):
            Rd1=30-bdate
        else:
            Rd1=31-bdate
            
        if bmonth-month==1 and bmonth==1:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==2:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==3:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==4:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==5:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==6:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==7:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==8:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==9:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==10:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==11:
            cdays2=Rd1+date
        elif bmonth-month==1 and bmonth==12:
            cdays2=Rd1+date
        elif month==1 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+date
        elif month==1 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+date
        elif month==1 and bmonth==10:
            cdays2=Rd1+Nov+Dec+date
        elif month==1 and bmonth==11:
            cdays2=Rd1+Dec+date
        elif month==1 and bmonth==12:
            cdays2=Rd1+date
        elif month==2 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+date
        elif month==2 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+date
        elif month==2 and bmonth==11:
            cdays2=Rd1+Dec+Jan+date
        elif month==2 and bmonth==12:
            cdays2=Rd1+Jan+date
        elif month==3 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+date
        elif month==3 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+date
        elif month==3 and bmonth==12:
            cdays2=Rd1+Jan+Fab+date
        elif month==4 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+date
        elif month==4 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+date
        elif month==5 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+date
        elif month==5 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+date
        elif month==5 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+Fab+Mar+Apr+date
        elif month==5 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+Mar+Apr+date
        elif month==5 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+Apr+date
        elif month==5 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+date
        elif month==6 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+date
        elif month==6 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+date
        elif month==6 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+Mar+Apr+May+date
        elif month==6 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+Apr+May+date
        elif month==6 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+May+date
        elif month==7 and bmonth==9:
            cdays2=Rd1+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+date
        elif month==7 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+date
        elif month==7 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+Apr+May+Jun+date
        elif month==7 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+May+Jun+date
        elif month==8 and bmonth==10:
            cdays2=Rd1+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+July+date
        elif month==8 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+Apr+May+Jun+July+date
        elif month==8 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+May+Jun+July+date
        elif month==9 and bmonth==11:
            cdays2=Rd1+Dec+Jan+Fab+Mar+Apr+May+Jun+July+Aug+date
        elif month==9 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+May+Jun+July+Aug+date
        elif month==10 and bmonth==12:
            cdays2=Rd1+Jan+Fab+Mar+Apr+May+Jun+July+Aug+Sep+date
        elif month==3 and bmonth==1:
            cdays2=Rd1+Fab+date
        elif month==4 and bmonth==1:
            cdays2=Rd1+Fab+Mar+date
        elif month==4 and bmonth==2:
            cdays2=Rd1+Mar+date
        elif month==5 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+date
        elif month==5 and bmonth==2:
            cdays2=Rd1+Mar+Apr+date
        elif month==5 and bmonth==3:
            cdays2=Rd1+Apr+date
        elif month==6 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+date
        elif month==6 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+date
        elif month==6 and bmonth==3:
            cdays2=Rd1+Apr+May+date
        elif month==6 and bmonth==4:
            cdays2=Rd1+May+date
        elif month==7 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+date
        elif month==7 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+date
        elif month==7 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+date
        elif month==7 and bmonth==4:
            cdays2=Rd1+May+Jun+date
        elif month==7 and bmonth==5:
            cdays2=Rd1+Jun+date
        elif month==8 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+Jul+date
        elif month==8 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+Jul+date
        elif month==8 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+date
        elif month==8 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+date
        elif month==8 and bmonth==5:
            cdays2=Rd1+Jun+Jul+date
        elif month==8 and bmonth==6:
            cdays2=Rd1+Jul+date
        elif month==9 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+Jul+Aug+date
        elif month==9 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+Jul+Aug+date
        elif month==9 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+Aug+date
        elif month==9 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+date
        elif month==9 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+date
        elif month==9 and bmonth==6:
            cdays2=Rd1+Jul+Aug+date
        elif month==9 and bmonth==7:
            cdays2=Rd1+Aug+date
        elif month==10 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+date
        elif month==10 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+Jul+Aug+Sep+date
        elif month==10 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+Aug+Sep+date
        elif month==10 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+Sep+date
        elif month==10 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+date
        elif month==10 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+date
        elif month==10 and bmonth==7:
            cdays2=Rd1+Aug+Sep+date
        elif month==10 and bmonth==8:
            cdays2=Rd1+Sep+date
        elif month==11 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+date
        elif month==11 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+date
        elif month==11 and bmonth==8:
            cdays2=Rd1+Sep+Oct+date
        elif month==11 and bmonth==9:
            cdays2=Rd1+Oct+date
        elif month==12 and bmonth==1:
            cdays2=Rd1+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==2:
            cdays2=Rd1+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==3:
            cdays2=Rd1+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==4:
            cdays2=Rd1+May+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==5:
            cdays2=Rd1+Jun+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==6:
            cdays2=Rd1+Jul+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==7:
            cdays2=Rd1+Aug+Sep+Oct+Nov+date
        elif month==12 and bmonth==8:
            cdays2=Rd1+Sep+Oct+Nov+date
        elif month==12 and bmonth==9:
            cdays2=Rd1+Oct+Nov+date
        elif month==12 and bmonth==10:
            cdays2=Rd1+Nov+date

        ld=int(cyear/4)
    
        cdays=cdays1+cdays2+ld
        cweeks=cdays/7
        yy=float(cdays/365)
        
        print("")
        print("You have been wasting Oxygen for : \n")
    
        print(yy," Years,")
        print(cmonth," Months,")
        print(cweeks," Weeks and")
        print(cdays," Days")
        
    if month==bmonth:
        
        if (year%10==0) or (byear%10==0):
            
            cyear=year-byear
            cyear1=cyear-1
            cdays1=cyear1*365
            
        
            if bmonth==2:
                Rd2=28-bdate
            elif bmonth==(4 or 6 or 9 or 11):
                Rd2=30-bdate
            else:
                Rd2=31-bdate
        
            if month==1 and bmonth==1:
                cdays2=Rd2+date+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec
            elif month==2 and bmonth==2:
                cdays2=Rd2+date+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan
            elif month==3 and bmonth==3:
                cdays2=Rd2+date+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab
            elif month==4 and bmonth==4:
                cdays2=Rd2+date+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar
            elif month==5 and bmonth==5:
                cdays2=Rd2+date+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr
            elif month==6 and bmonth==6:
                cdays2=Rd2+date+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May
            elif month==7 and bmonth==7:
                cdays2=Rd2+date+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun
            elif month==8 and bmonth==8:
                cdays2=Rd2+date+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul
            elif month==9 and bmonth==9:
                cdays2=Rd2+date+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug
            elif month==10 and bmonth==10:
                cdays2=Rd2+date+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep
            elif month==11 and bmonth==11:
                cdays2=Rd2+date+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct
            elif month==12 and bmonth==12:
                cdays2=Rd2+date+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov

            ld=int(cyear/4)
        
            cdays=cdays1+cdays2+ld
            cweeks=cdays/7
            yy=float(cdays/365)
            
            print("")
            print("You have been wasting Oxygen for : \n")
    
            print(yy," Years,")
            print(cmonth," Months,")
            print(cweeks," Weeks and")
            print(cdays," Days")
        else:
        
            cdays1=(cyear-1)*365
            cyear1=cyear-1
            
            if bmonth==2:
                Rd2=28-bdate
            elif bmonth==(4 or 6 or 9 or 11):
                Rd2=30-bdate
            else:
                Rd2=31-bdate
        
            if month==1 and bmonth==1:
                cdays2=Rd2+date+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec
            elif month==2 and bmonth==2:
                cdays2=Rd2+date+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan
            elif month==3 and bmonth==3:
                cdays2=Rd2+date+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab
            elif month==4 and bmonth==4:
                cdays2=Rd2+date+May+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar
            elif month==5 and bmonth==5:
                cdays2=Rd2+date+Jun+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr
            elif month==6 and bmonth==6:
                cdays2=Rd2+date+Jul+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May
            elif month==7 and bmonth==7:
                cdays2=Rd2+date+Aug+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun
            elif month==8 and bmonth==8:
                cdays2=Rd2+date+Sep+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul
            elif month==9 and bmonth==9:
                cdays2=Rd2+date+Oct+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug
            elif month==10 and bmonth==10:
                cdays2=Rd2+date+Nov+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep
            elif month==11 and bmonth==11:
                cdays2=Rd2+date+Dec+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct
            elif month==12 and bmonth==12:
                cdays2=Rd2+date+Jan+Fab+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov

            ld=int(cyear/4)
        
            cdays=cdays1+cdays2+ld
            cweeks=cdays/7
            yy=float(cdays/365)
            
            print("")
            
            return "You have been wasting Oxygen for : \n\n"+str(yy)+" Years,\n"+str(cmonth)+" Months,\n"+str(cweeks)+" Weeks and\n"+str(cdays)+" Days\n"

def send():
    
    date=datetime.datetime.now()
    y=date.year
    m=date.month
    d=date.day
    dict={}
    dict1={}
    dict2={}
    dict3={}
    dcal=[]
    mcal=[]
    sendlist=[]
    
    dates=pd.read_excel("birth1.xlsx")
    yearlist=dates["Year"].tolist()
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
	
    for i in range(len(maillist)):
        dict3[maillist[i]]=yearlist[i]

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
            for k in dict3:
                if i==j and k==j:
                    f=open("days.txt","w")
                    f.write(dmycalculateCModule(dict3[k]))
                    f.close()
                   
                    contacts = [keys]
                    msg = EmailMessage()
                    msg['Subject'] = 'Happy Birthday'
                    msg['From'] = "example@gmail.com"
                    msg['To'] = j
                    msg.set_content('Happy Birthday '+dict2[i])
            

                    with open("days.txt","rb") as f:
                        file_data=f.read()
                        file_name=f.name
                    
                    msg.add_attachment(file_data,maintype="text",subtype="file_type", filename=file_name)
         
                    try:
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login("example77@gmail.com", "*******")
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
