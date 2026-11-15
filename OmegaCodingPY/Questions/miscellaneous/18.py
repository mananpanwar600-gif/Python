'''
 Print Alternate Prime Numbers till 20
A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

For example:

All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19

Alternate prime numbers from 1 to 20:
2, 5, 11, 17
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = 20
primes = [] 
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)


print(f"All prime numbers from 1 to {n}: {primes}")


print(f"Alternate prime numbers from 1 to {n}:")

for i in range(0, len(primes), 2): 
    print(primes[i])