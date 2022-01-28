from sys import *
import display as d

def main():
	
    print("\n----DISPLAY FILE-----\n")
    
    if len(argv)>3 or len(argv)<2 or len(argv)==1:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : This is used to Displya all Files with Given Extension.")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : DIRECTORY_NAME EXTENSION")
        else:
            print("No such Flag Exists")
    
    if len(argv)==3:
        try:
            dname=argv[1]
            ename=argv[2]
            d.display(dname,ename)
        except Exception as c:
            print(c)
            quit()

if __name__=="__main__":
	main()
