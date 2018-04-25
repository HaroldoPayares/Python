from math import sqrt

def fibonacci(n):

    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

def main():

    print("How many numbers of the fibonacci series do you want to print?: ", end=' ')
    answer = int(input())

    print(fibonacci(answer))

if __name__ == "__main__":
    
    main()
