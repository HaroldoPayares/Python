from math import sqrt

def fibonacci(n):

    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

def main():

    print("Please type the position number of the fibonacci series you want to check: ", end=' ')
    answer = int(input())

    print(fibonacci(answer))

if __name__ == "__main__":
    
    main()
