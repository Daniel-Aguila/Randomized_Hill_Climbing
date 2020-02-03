import math
import numpy as np


def RHC(sp, p, z, seed):
    np.random.seed(seed)
    x = sp[0]
    y = sp[1]

    optimalF = math.pow((math.pow(x, 2) + y - 11), 2) + math.pow((x + math.pow(y, 2) - 7), 2)
    numSol = 0
    for i in range(p):
        z1 = np.random.uniform(-z, z)
        z2 = np.random.uniform(-z, z)
        x += z1
        y += z2
        minimizeF = math.pow((math.pow(x, 2) + y - 11), 2) + math.pow((x + math.pow(y, 2) - 7), 2)
        if optimalF > minimizeF:
            optimalF = minimizeF
            numSol += 1

    vector = (x, y)
    return vector, optimalF, numSol


def main():
    seed = 5  # 5 Is close but NOT TO MY STANDARDS
    sp = (2,0)
    p = 30
    z = 0.03

    print(RHC(sp, p, z, seed))

    return


if __name__ == '__main__':
    main()
