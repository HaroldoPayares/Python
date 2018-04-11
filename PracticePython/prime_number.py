# This program checks is the number is prime or composite
import sys

print("Please enter a natural number to determine if is prime or composite: ", end='')
number_to_analyze = int(input())

# count from 1 to the actual value of number_to_analyze variable
counter = 1
# if "number_to_analyze" is evenly divisible by the current "counter" value,
# check will increase it's value by one
check = 0

if number_to_analyze < 2:

    print("Composite or prime numbers are naturals numbers greater than 1")
    sys.exit()

elif number_to_analyze > 2:
# loop to determine how many numbers divide evenly "number_to_analyze"
    while counter <= number_to_analyze:
        # operation to test if number is evenly divided
        test = number_to_analyze % counter
        # if number is evenly divided then check will add 1 to it self
        if test == 0:
            check += 1
        # counter add 1 to it self before the loop start again
        counter +=1

    if check == 2:

        print(f"The number {number_to_analyze} is prime")

    elif check > 2:

        print(f"The number {number_to_analyze} is composite")

else:

    print(f"The number {number_to_analyze} is prime")
