import random

def argmax(choices, criteria, args=None):
    m = max(criteria(c, args) for c in choices)
    return random.choice(list(filter(lambda c: criteria(c, args) == m, choices)))

def check_equal_shapes(*arrs):
    return len({a.shape for a in arrs}) == 1
