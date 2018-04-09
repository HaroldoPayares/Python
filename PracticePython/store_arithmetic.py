from sys import argv,exit
import time

script, filename = argv

print("Let's do some arithmetics with two numbers")
print("Would you like to an addition or substraction?", end=' ')
option = input()

if option == 'addition':
    
    print("Enter the first number:", end=' ')
    first_number = int(input())
    
    print("Enter the second number:", end=' ')
    second_number = int(input())
    
    value = first_number + second_number
    
    text_to_store = f"The number {first_number} plus {second_number} equals {value}"
    
    print(text_to_store)
    
    target_file = open(filename, 'a+')
    
    print("Saving the results...")
    target_file.write(text_to_store)
    time.sleep(5)
    target_file.close()

elif option == 'substraction':
    
    print("Enter the first number:", end=' ')
    first_number = int(input())
    
    print("Enter the second number:", end=' ')
    second_number = int(input())
    
    value = first_number - second_number
    
    text_to_store = str(f"The number {first_number} minus {second_number} equals {value}")
    
    print(text_to_store)
    
    target_file = open(filename, 'a+')
    
    print("Saving the results...")
    target_file.write(text_to_store)
    time.sleep(5)
    target_file.close()
    print("Data saved")

else:
    print("You should type 'addition' or 'substraction")
    exit(0)

