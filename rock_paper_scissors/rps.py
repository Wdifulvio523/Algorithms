#!/usr/bin/python

import sys

def rock_paper_scissors(n):

  # define possible plays, and make list of  possibleoutcomes 
  outcomes = [] 
  plays = ['rock', 'paper', 'scissors']

  # make helper function that can take the rounds left (n), and the result(empty [])
  def helper(roundsLeft, result):

    # if there are no rounds left, it will take all the results 
    # and put it in the outcomes array
    if roundsLeft == 0:
      outcomes.append(result)
      return
    # as long as there are plays left, for every item in the plays array, 
    # it will add it to the results array  
    for play in plays:
      helper(roundsLeft - 1, result + [play])

  #  call the helper function, and return the outcomes array to get your answer
  helper(n,[])
  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')