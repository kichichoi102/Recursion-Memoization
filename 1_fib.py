def fib(n):
    if n <= 2:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(0))
print(fib(4))
print(fib(10))
print(fib(14))
