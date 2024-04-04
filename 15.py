# with use library 

import math

n = 20

routes = math.comb(2*n, n)

print("The number of paths in a network {}x{}: {}".format(n, n, routes))



# with out library 

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = 20

routes = factorial(2*n) // (factorial(n) ** 2)

print("The number of paths in a network {}x{}: {}".format(n, n, routes))


# result : 137846528820
