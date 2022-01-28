from sys import *
import copy as cc

def main():

    print("\n----COPY FILE-----\n")
    
    if len(argv)>3 or len(argv)<2 or len(argv)==1:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : This is used to Copy all Files From A Directory to Another")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : FROM_DIRECTORY_NAME TO_DIRECTORY_NAME")
        else:
            print("No such Flag Exists")
    
    if len(argv)==3:
        try:
            dfname=argv[1]
            dyname=argv[2]
            cc.copy(dfname,dyname)
        except Exception as c:
            print(c)
            exit()

if __name__=="__main__":
	main()
