from sys import *
import copyex as cx

def main():

    print("\n----COPY FILE(EXT)-----\n")
    
    if len(argv)>4 or len(argv)<2 or len(argv)==3:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : This is used to Copy all Files From a Directory to Another Having the Given Exension")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : FROM_DIRECTORY_NAME TO_DIRECTORY_NAME EXTENSION")
        else:
            print("No such Flag Exists")
    
    if len(argv)==4:
        try:
            dfname=argv[1]
            dyname=argv[2]
            ename=argv[3]
            cx.copyex(dfname,dyname,ename)
        except Exception as c:
            print(c)
            exit()

if __name__=="__main__":
	main()
