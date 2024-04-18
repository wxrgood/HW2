import numpy as np

def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    results = numvec.astype(object)
    results[(numvec % 3 == 0) & (numvec % 5 != 0)] = 'Fizz'
    results[(numvec % 5 == 0) & (numvec % 3 != 0)] = 'Buzz'
    results[(numvec % 3 == 0) & (numvec % 5 == 0)] = 'FizzBuzz'
    return results
