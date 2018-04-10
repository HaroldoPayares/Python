from sys import argv,exit
import time

script, filename = argv

print("Would you like to erase the file, yes or no?:", end='')
option = input()

if option == 'yes':
    
    open(filename,'w').close()

    print("Deleting the containing data...")
    time.sleep(3)

elif option == 'no':

    print("See you later..")
    exit(0)

else:

    print("you should type 'yes' or 'no'")
    exit(0)
