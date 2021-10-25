
from time import time

def factorize(number):  
    max_factor = number
    factors = []
    for i in range(1,(number+1)):
        if number % i == 0:
            factors.append(i)
            max_factor = int(number / i)
            factors.append(max_factor)
        if i > max_factor:
            break
    unique_factors = list(set(factors))
    return len(unique_factors) 

i = 1
list_primes = []


end = time() + 300
while time() < end:
    if factorize(i) == 2:
        list_primes.append(i)
    i += 1


print(len(list_primes))


