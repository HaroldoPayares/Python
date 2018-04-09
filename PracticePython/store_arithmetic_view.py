from sys import argv,exit
import time

script, filename = argv

print("Would you like to check the stored aithmetics?(enter 'yes' or 'no')", end=' ')
option = input()

if option == 'yes':

    with open(filename,'r') as file_to_check:

        file_to_check.seek(0)
        print(file_to_check.read())

        print("\nNow clousing file...")
        time.sleep(3)
        print("File closed")

elif option == 'no':

    print("Good bye")
    exit(0)

else:

    print("You should type 'yes' or 'no'")
