import sys
import time
import itertools
import cProfile
import pstats
import io

import prime_divide
import prime_pq
import wheel

with open("P-1000000.txt", "r") as f:
    table = [int(l.split(", ")[1]) for l in f]

def timeitall(pg, check, legend):
    start = time.time_ns()
    last = next(itertools.islice(pg, check-1, check))
    stop = time.time_ns()
    assert last == table[check-1]
    print(round((stop-start) / 1_000_000_000, 3), legend)
    sys.stdout.flush()
    return stop-start

def profile(pg, check):
    pr = cProfile.Profile()
    pr.enable()
    last = next(itertools.islice(pg, check-1, check))
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.CUMULATIVE)
    ps.print_stats()
    print(s.getvalue())
    assert last == table[check-1]

def main():
    #timeitall(prime_divide.primes(), 10000, "Divide")
    #timeitall(prime_pq.sieve(itertools.count(2)), 10000, "Priority Queue")
    timeitall(itertools.chain([2, 3, 5, 7],
                              prime_pq.sieve(wheel.wheel([2, 3, 5, 7]))),
                                             10000, "Priority Queue")
    #for p in itertools.islice(prime_pq.sieve(itertools.count(2)), 10):
    #    print(p)


    #profile(prime_divide.primes(), 10000)

if __name__ == "__main__":
    main()
