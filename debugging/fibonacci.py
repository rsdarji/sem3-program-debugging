def fibonacci(n):
    a = 0
    b = 1
    c = 0
    print(n)
    while n >= 0:
        print(c + a)
        a, b = b, a + b
        n -= 1

    return b

if __name__ == '__main__':
    n = input('Please enter the Fibonacci number you want to computer: ')
    fib = fibonacci(int(n))
    print('Answer:', fib)


