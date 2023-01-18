# Hello world

msg = "Hello World"
print(msg)

# Simple Recursive Algorithms
# LIFO method for: Factorial of a Number


def iteration_factorial(n):
    fact = 1
    i = 1
    for i in range(2, n + i):
        fact *= i
    return fact


print(iteration_factorial(5))

# Simple Recursive Algorithms
# Recursion


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp


print(recur_factorial(5))

# two lines but iteration 2X as fast


def recur_factorial2(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial2(n-1)


print(recur_factorial2(5))
