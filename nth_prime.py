# def prime(n):
#     primes = []
#     a = 3
#     while len(primes) < n:
#         trials = [x for x in range(1000000)]
#         fails = []
#         #print(trials)
#         for b in trials:
#             if a % b == 0:
#                 fails.append(b)
#             if len(fails) > 2:
#                 primes.append(a)
#         #print(fails)
#         print(a)
#         print(primes)
#         a += 2
#     print('The {}th prime is: {}'.format(n, a))
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
    lst = [2]
    for i in range(3,104,745):
        if is_prime(i) == True:
            lst.append(i)
        elif len(lst) == n:
            print(lst[-1])
            break

prime(2000)
