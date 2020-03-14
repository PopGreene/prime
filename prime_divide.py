import itertools

def primes():
    ps = []
    for n in itertools.count(2):
        if not any( n % p == 0 for p in ps ):
            ps.append(n)
            yield n
