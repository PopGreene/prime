import itertools

def primes():
    ps = []
    sieves = []
    for n in itertools.count(2):
        isPrime = True
        for m, (p, s) in enumerate(zip(ps, sieves)):
            if s == 0:
                sieves[m] = p-1
                isPrime = False
            else:
                sieves[m] -= 1
        if isPrime:
            ps.append(n)
            sieves.append(n-1)
            yield n
