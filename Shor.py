import random
import math


def gcd(a, b):
    return math.gcd(a, b)


def shor_factor(N):

    if N % 2 == 0:
        return 2

    while True:
        
        a = random.randint(2, N - 2)

        
        g = gcd(a, N)
        if g > 1:
            return g

        
        r = 1
        while pow(a, r, N) != 1:
            r += 1

        
        if r % 2 != 0:
            continue

        x = pow(a, r // 2, N)

        if x == N - 1:
            continue

        
        factor1 = gcd(x - 1, N)
        factor2 = gcd(x + 1, N)

        if factor1 not in [1, N]:
            return factor1
        if factor2 not in [1, N]:
            return factor2


if __name__ == "__main__":
    N = 15  
    factor = shor_factor(N)

    print("Number:", N)
    print("Factor found:", factor)
    print("Other factor:", N // factor)