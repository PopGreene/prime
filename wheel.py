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
