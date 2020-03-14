import itertools
import functools

def mask(n):
    while True:
        for i in range(n-1):
            yield False
        yield True

def primes():
    sieve = []
    for n in itertools.count(2):
        if not functools.reduce(lambda x, y: next(y) or x, sieve, False):
            yield n
            sieve.append(mask(n))
