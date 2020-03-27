import heapq

def sieve(ng):
    x = next(ng)
    heap = [(x*x, x)]
    yield x

    for x in ng:
        c, p = heap[0]
        while x > c:
            heapq.heappushpop(heap, (c+p, p))
            c, p = heap[0]
        if x != c:
            heapq.heappush(heap, (x*x, x))
            yield x
