# Program to check if number is even or odd
print("This program will check if the number is even or odd,\n Please enter a number:", end='')
number = int(input())

check = number % 2

if check == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
