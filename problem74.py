import numpy as np

1000000
starting_numbers = np.arange(1,1000001)

counter = 0

def find_factorial_sum(n):
    digits = str(n).split()
    return sum([np.factorial(int(d)) for d in digits])


