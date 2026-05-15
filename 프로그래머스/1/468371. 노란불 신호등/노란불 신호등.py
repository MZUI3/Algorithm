from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    periods = [g + y + r for g, y, r in signals]

    LIMIT = reduce(lcm, periods)

    g0, y0, r0 = signals[0]
    p0 = periods[0]

    for base in range(0, LIMIT, p0):

        for d in range(1, y0 + 1):
            t = base + g0 + d

            if t > LIMIT:
                break

            ok = True

            for g, y, r in signals[1:]:
                p = g + y + r

                x = (t - 1) % p + 1

                if not (g < x <= g + y):
                    ok = False
                    break

            if ok:
                return t

    return -1