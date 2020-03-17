import sys
import itertools
import pqdict

def sieve(ng):
    x = next(ng)
    g = itertools.count(x*x,x)
    pq = pqdict.pqdict({x:(next(g),g)}, key=lambda x:x[0])
    yield x

    for x in ng:
        p, (c, g) = pq.topitem()
        if x == c:
            print("Composite:", x)
            while x == c:
                pq.updateitem(p, (next(g),g))
                p, (c, g) = pq.topitem()
        else:
            print("Prime:", x)
            sys.stdout.flush()
            assert x < c, f"{x} {c}"
            g = itertools.count(x*x,x)
            pq[x] = (next(g), g)
            yield x
