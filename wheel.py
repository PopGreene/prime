# Produces an infinite list of numbers that are relatively prime to the
# provided numbers - which should be prime.  The numbers are provided in a list.
# Examples:
#     number_generator = wheel([2, 3, 5, 7])

import itertools
import functools
import operator

def wheel(pl):
    circ = functools.reduce(operator.mul, pl)
    masks = ( itertools.cycle([1]*(n-1) + [0]) for n in pl )
    mask = ( functools.reduce(operator.and_, col) for col in zip(*masks) )
    ints = list( itertools.compress(range(1,circ+2), mask) )
    steps = [ x - y for x, y in zip(ints[1:], ints[:-1]) ]
    nextp = 1
    while steps:
        for step in steps:
            nextp += step
            yield nextp

def addWheel(p, wh=None):
    if not wh:
        return [p]
    new_wheel = []
    wa = 0
    wv = 1
    pv = p
    for v in wh * p:
        wv += v
        wa += v
        while pv < wv:
            pv += p
        if pv != wv:
            new_wheel.append(wa)
            wa = 0
    return new_wheel