import pqdict

def sieve(ng):
    x = next(ng)
    pq = pqdict.pqdict({x:x*x})
    yield x

    for x in ng:
        p, c = pq.topitem()
        while x > c:
            pq.updateitem(p, c+p)
            p, c = pq.topitem()
        if x != c:
            pq[x] = x*x
            yield x
