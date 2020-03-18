import sys
import itertools
import heapq

def sieve(ng):
    try:
        x = next(ng)
    except KeyError:
        return

    n = itertools.count()
    g = itertools.count(x*x, x)
    heap = [(next(g), next(n), g)]
    yield x

    for x in ng:
        (c, _, g) = heap[0]
        while x > c:
            heapq.heappushpop(heap, (next(g), next(n), g))
            (c, _, g) = heap[0]
        if x != c:
            assert x < c, f"{x} {c}"
            g = itertools.count(x*x, x)
            heapq.heappush(heap, (next(g), next(n), g))
            yield x
