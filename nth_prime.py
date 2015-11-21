
def is_prime(x):
    if x == 2:
        return True
    else:
        for number in range (3,x):
            if x % number == 0 or x % 2 == 0:
         #print number
                return False

        return True

def prime(n):
    primes = [2]
    for i in range(3, 1000000):
        if is_prime(i) == True:
            primes.append(i)
        elif len(primes) == n:
            return primes[-1]
    #print("The {}th prime is {}".format(n, primes[-1]))
