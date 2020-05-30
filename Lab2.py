import math
import random

N = 10 ** 100
M = 10 ** 4
res = (6 / math.pi ** 2) + (math.log(10 ** 100) / (10 ** 100))

def lab(M):
    S = 0
    for x in range(M):
        a = random.randint(1, N)
        b = random.randint(1, N)
        if b > a:
            a, b = b, a
        R = a % b

        while R > 0:
            a, b = b, R
            R = a % b
            if R == 1:
                S = S + 1
    print('Probability:', S / M)
    print('Teoreth: ', res)

print(lab(M))