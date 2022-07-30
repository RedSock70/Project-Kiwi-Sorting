from random import randint, random
from select import select
from SelectSortKiwi import bubble
from time import time

avaragecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(avaragecase)
worstcase= sorted(avaragecase, reverse=True) 

def test_SelectWorst():
    start= time
    assert select(worstcase) == bestcase
    print(time()-start)

def test_SelectBest():
    start= time
    assert select(bestcase) == bestcase
    print(time()-start)    
    
def test_SelectAvg():
    start= time
    assert select(avaragecase) == bestcase
    print(time()-start)