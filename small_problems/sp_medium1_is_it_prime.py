# This stops looping at n // 2, but the real stop condition should have been sqrt(n)

def is_prime(num):
    if num <= 0 or not isinstance(num, int):
        raise TypeError("Natural numbers only please")
    if num == 1:
        return False
    if num == 2:
        return True
    for n in range(2, max(num // 2, 3)):
        if num % n == 0:
            return False
    return True



print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
print(is_prime(91) == False)
