#!/usr/bin/python

import math
import operator


def recipe_batches(recipe, ingredients):
    # get the maximum value from ingredients.items, so we have a starting point
    batches = max(ingredients.items(), key=operator.itemgetter(1))[1]
    # loop through the recipes dict
    for rkey in recipe.items():
        # if the key from recipes does NOT appear in ingredients, batches = 0 because
        # we cannot make the recipe
        if rkey[0] not in ingredients.keys():
            batches = 0
        # loop through the ingredients dict
        for ikey in ingredients.items():
            # if the key of ingredients matches the key of recipe
            if ikey[0] == rkey[0]:
                # check whether we have more in ingredients than the recipe calls for
                if ikey[1] > rkey[1]:
                    # if so, check whether the division is smaller than the current total
                    #  number of batches we can make
                    if (ikey[1] // rkey[1]) < batches:
                        # if it is lower, then we decrease the total number of batches we can
                        # make to this new total
                        batches = (ikey[1] // rkey[1])
    # return total number of batches we can make
    return batches

  ## TIME COMPLEXITY: O(n^2) ? I think? Thats pretty bad



if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
    ingredients = {'milk': 298, 'butter': 202, 'cheese': 100}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
