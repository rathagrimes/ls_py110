import math

# Write a function called fibonacci that computes the nth Fibonacci
# number, where nth is an argument passed to the function.
#
# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)


# Need to retain the last 2 
def fib_iter(n):
    prev, last = 1, 1
    if n in [1, 2]:
        return 1
    for _ in range(2, n):
        prev, last = last, prev + last
    return last
    
def fib_recur(n):
    if n in [1, 2]:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)
    
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in [1, 2]:
        return 1
    if n in memo:
        return memo[n];
    result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    memo[n] = result

    return result

def fibonacci(n):
    return fib_memo(n)

# print(fibonacci(1) == 1)                  # True
# print(fibonacci(2) == 1)                  # True
# print(fibonacci(3) == 2)                  # True
# print(fibonacci(4) == 3)                  # True
# print(fibonacci(5) == 5)                  # True
# print(fibonacci(6) == 8)                  # True
# print(fibonacci(12) == 144)               # True
# print(fibonacci(20) == 6765)              # True
# print(fibonacci(50) == 12586269025)       # True
# print(fibonacci(75) == 2111485077978050)  # True


# Write a function that calculates and returns the index of the first
# Fibonacci number that has the number of digits specified by the
# argument. The first Fibonacci number has an index of 1. You may assume
# that the argument is always an integer greater than or equal to 2.

def get_num_length(num):
    if num == 1:
        return 1
    return math.ceil(math.log10(num))

def find_fibonacci_index_by_length(length):
    cur = 1
    while True:
        fib = fib_iter(cur)
        
        if get_num_length(fib) >= length:
        # The following was 2 seconds slower
        #if fib >= 10 ** (length - 1):
            return cur

        cur += 1

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
# NOTE: Took 5 minutes on my ThinkPad x13 under WSL
print("Wait for it...")
print(find_fibonacci_index_by_length(10000) == 47847)


# print(get_num_length(1) == 1)
# print(get_num_length(1.00001) == 1)
# print(get_num_length(5) == 1)
# print(get_num_length(9) == 1)
# print(get_num_length(18) == 2)
# print(get_num_length(98765) == 5)
# print(get_num_length(987654321) == 9)
