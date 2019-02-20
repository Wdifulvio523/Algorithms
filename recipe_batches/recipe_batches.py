#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  whole_batches = {}
  for rkey in recipe.items():
  
    for ikey in ingredients.items():

      if rkey[0] == ikey[0]:
        batches = math.floor(ikey[1]/ rkey[1])
        print("batches, keys", ikey[1], rkey[1],  batches)
        if rkey not in whole_batches:
          print("batches",batches)
          print("batches not in whole batches, adding")
          whole_batches[rkey] = batches
        elif batches > whole_batches[batches]:
          print("do we ever get here?")
          whole_batches[batches] = batches
          print("while batches", whole_batches)
  
  return whole_batches[batches]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 55, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))