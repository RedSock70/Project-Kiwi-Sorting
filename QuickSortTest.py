from random import randint, random
from Quicksortkiwi import quickSort
from time import time

avaragecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(avaragecase)
worstcase= sorted(avaragecase, reverse=True) 

def test_QuickWorst():
    start= time
    assert quickSort(worstcase) == bestcase
    print(time()-start)

def test_QuickBest():
    start= time
    assert quickSort(bestcase) == bestcase
    print(time()-start)    
    
def test_QuickAvg():
    start= time
    assert quickSort(avaragecase) == bestcase
    print(time()-start)