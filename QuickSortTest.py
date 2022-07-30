from random import randint, random
import numpy as np
from Quicksortkiwi import quickSort, data
from time import time

# avaragecase= [randint(1,10000) for _ in range(1000)]
# bestcase= sorted(avaragecase)
# worstcase= sorted(avaragecase, reverse=True) 
avaragecase = data
bestcase = np.sort(avaragecase)
worstcase = bestcase[::-1]
def test_QuickWorst():
    start= time()
    assert np.array_equal( quickSort( np.copy(worstcase), 0, len(worstcase)-1) , bestcase)
    print(str(time()-start))

def test_QuickBest():
    start= time()
    assert np.array_equal( quickSort( np.copy(bestcase), 0, len(bestcase)-1) , bestcase)
    print(str(time()-start))
    
def test_QuickAvg():
    start= time()
    assert np.array_equal( quickSort( np.copy(avaragecase), 0, len(avaragecase)-1) , bestcase)
    print(str(time()-start))