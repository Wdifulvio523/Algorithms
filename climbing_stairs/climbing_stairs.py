#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    # define maxmimum number of steps 
    MAX_STEP = 3
    # check if cache is none. if so, make it a list who's length is num
    if cache is None:
        cache = [0] * n
    # handling for negative
    if n < 0:
        return 0
    # handling for zero
    elif n == 0:
        return 1
    
    else:
        #variable for total number of possibilities
        total = 0
        # loop through a range of max steps, starting at max and stopping at 0
        for step in range(MAX_STEP, 0, -1):
            # variable that points to n minus current step
            stairs_after_step = n - step
            #if above variable is negative, move on
            if stairs_after_step < 0:
                continue
            # if variable does not appear in cache
            if cache[stairs_after_step] == 0:
                # recursively run climbing stairs, with variable as incoming n
                cache[stairs_after_step] = climbing_stairs(
                    stairs_after_step, cache)
            # add the variable to total
            total += cache[stairs_after_step]

        return total


print(climbing_stairs(1))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
