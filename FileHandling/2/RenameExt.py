from sys import *
import rename as r

def main():

    print("\n----RENAME FILE-----\n")
    
    if len(argv)>4 or len(argv)<2:
        print("INVALID ARGUMENT\nEnter -u for Usage\nEnter -h for Help")
    
    if len(argv)==2:
        if argv[1]=="-u" or argv[1]=="-U":
            print("USAGE : This is used to Rename all Files with Given Extension.")
        elif argv[1]=="-h" or argv[1]=="-H":
            print("HELP : DIRECTORY_NAME FROM_EXTENSION TO_EXTENSION")
        else:
            print("No such Flag Exists")
    
    if len(argv)==4:
        try:
            dname=argv[1]
            efname=argv[2]
            etname=argv[3]
            r.rename(dname,efname,etname)
        except Exception as c:
            print(c)
            quit()
	
if __name__=="__main__":
	main()
