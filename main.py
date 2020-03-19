import sys
import time
import itertools
import cProfile
import pstats
import io

import prime_divide
import prime_pq
import prime_heapq
import wheel

wheelie = [ 2, 3, 5, 7 ]

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
    timeitall(prime_divide.primes(), 10000, "Divide")
    timeitall(prime_pq.sieve(itertools.count(2)), 10000, "Priority Queue")
    timeitall(prime_heapq.sieve(itertools.count(2)), 10000, "Heap")
    timeitall(itertools.chain(wheelie,
                              prime_pq.sieve(wheel.wheel(wheelie))),
                                             10000, "Prority Queue Wheel")
    timeitall(itertools.chain(wheelie,
                              prime_heapq.sieve(wheel.wheel(wheelie))),
                                                10000, "Heap Wheel")
    #for p in itertools.islice(prime_heap.sieve(itertools.count(2)), 10):
    #    print(p)


    #profile(prime_divide.primes(), 10000)

if __name__ == "__main__":
    main()
