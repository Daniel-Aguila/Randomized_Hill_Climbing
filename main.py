import math
#import matplotlib.pyplot as plt
import random

#matplotlib has been commented out due to the case of the program not having the opportunity to experience erros, when testing
#In another computer where they are not imported properly.


#plt.ylabel('f(x,y)')
#plt.xlabel('iteration #')


def RHC(sp, p, z, seed):
    random.seed(seed)  # call seed
    x = sp[0]
    y = sp[1]
    numSol = 1
    # Optiomal Function for minimal
    optimalF = math.pow((math.pow(x, 2) + y - 11), 2) + math.pow((x + math.pow(y, 2) - 7), 2)
    f = optimalF
    flag = False
    # hI
    while f != optimalF or flag == False:
        flag = True
        f = optimalF
        for i in range(p):
            # Checks the radius around the point
            z1 = random.uniform(-z, z)
            z2 = random.uniform(-z, z)
            minimizeF = math.pow((math.pow((x + z1), 2) + (y + z2) - 11), 2) + math.pow(((x + z1) + math.pow((y + z2), 2) - 7), 2)
            if optimalF > minimizeF:  # Check if is lower, if so change it to optimal
                optimalF = minimizeF
                # If is optimal than the point 'moves'
                x += z1
                y += z2
                #plt.scatter(numSol,minimizeF, c="red")
                numSol += 1
    vector = (x, y)  # final value of the optimal vector.
    #plt.show()
    return vector, optimalF, numSol


def main():
    # variables
    seed = float(input("Enter seed: "))  # Find new seed that is better
    x = float(input("Input starting point X value: "))
    y = float(input("Input starting point Y value: "))
    sp = (x, y)  # Starting Point
    p = int(input("Input p-neighrbors: ")) # TODO understand if this is the range of the iterations in total, or does it reset every time?
    z = float(input("Input Z value: "))  # Radius of vision from the starting point

    print(RHC(sp, p, z, seed))
    return


if __name__ == '__main__':
    main()

