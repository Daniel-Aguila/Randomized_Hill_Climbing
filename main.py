import math
import numpy as np
import matplotlib.pyplot as plt

plt.ylabel('f(x,y)')
plt.xlabel('iteration #')

def RHC(sp, p, z, seed):
    np.random.seed(seed)  # call seed
    x = sp[0]
    y = sp[1]
    # Optiomal Function for minimal
    optimalF = math.pow((math.pow(x, 2) + y - 11), 2) + math.pow((x + math.pow(y, 2) - 7), 2)
    numSol = 1
    # hI
    for i in range(p):
        # Checks the radius around the point
        z1 = np.random.uniform(-z, z)
        z2 = np.random.uniform(-z, z)
        minimizeF = math.pow((math.pow((x+z1), 2) + (y+z2) - 11), 2) + math.pow(((x+z1) + math.pow((y+z2), 2) - 7), 2)
        if optimalF > minimizeF:  # Check if is lower, if so change it to optimal
            optimalF = minimizeF
            # If is optimal than the point 'moves'
            x += z1
            y += z2
            print(minimizeF, x, y)
            plt.scatter(i,optimalF)
            numSol += 1
    vector = (x, y)  # final value of the optimal vector.
    plt.show()
    return vector, optimalF, numSol


def main():
    # variables
    seed = 5  # Find new seed that is better
    sp = (-2, 3) # Starting Point
    p = 100  # TODO understand if this is the range of the iterations in total, or does it reset every time?
    z = 0.03 # Radius of vision from the starting point

    RHC(sp, p, z, seed)
    return


if __name__ == '__main__':
    main()
