#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # make new variable for all coins besides pennies
    coins = [5, 10, 25, 50]
    # create a cache list for amount
    cache = [1] * (amount + 1)
    # loop through coins 
    # (complexity = length of coins list?)
    for coin in coins:
        # loop through range from coin to amount 
        # (complexity = N * amount - coin?)
        for higherAmount in range(coin, amount + 1):
            #find difference between the current amount and the coin 
            change = higherAmount - coin
            # To the cache at the current amount, 
            # add the amount at the cache at change
            cache[higherAmount] += cache[change]
    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
