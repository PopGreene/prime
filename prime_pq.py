import sys
import itertools
import pqdict

def sieve(ng):
    try:
        x = next(ng)
    except KeyError:
        return

    g = itertools.count(x*x,x)
    pq = pqdict.pqdict({x:(next(g),g)}, key=lambda x:x[0])
    yield x

    for x in ng:
        p, (c, g) = pq.topitem()
        while x > c:
            pq.updateitem(p, (next(g),g))
            p, (c, g) = pq.topitem()
        if x != c:
            #print("Prime:", x)
            #sys.stdout.flush()
            assert x < c, f"{x} {c}"
            g = itertools.count(x*x,x)
            pq[x] = (next(g), g)
            yield x
