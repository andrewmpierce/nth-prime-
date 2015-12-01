
#Current problem to fix identified via testing: Gets caught in endless loop when number
#entered is below 3, does not raise errors for negative numbers.

def is_prime(x):
    if x == 2:
        return True
    else:
        for number in range (3,x):
            if x % number == 0 or x % 2 == 0:
                return False
        print("True")
        return True


def prime(n):
    primes = [2]
    for i in range(3, 1000000):
        if is_prime(i) == True:
            primes.append(i)
        elif len(primes) == n:
            print("The {}th prime is {}".format(n, primes[-1]))
            return primes[-1]

is_prime(2)
