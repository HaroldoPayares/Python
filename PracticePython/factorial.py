from sys import exit

def factorial(n):

    if n == 0:
        return 1
    elif n > 0:
        return n * factorial( n - 1)
    else:
        print("Number should be a natural number")
        exit(0)

def main():

    print("Let's do some factorials, type a natural number: ", end=' ')
    number = int(input())

    result = factorial(number)
    print(f"{number}! = {result}")

if __name__ == "__main__":
    main()
