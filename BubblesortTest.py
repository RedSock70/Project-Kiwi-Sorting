from random import randint, random
from BubbleSortKiwi import bubble
from time import time

avaragecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(avaragecase)
worstcase= sorted(avaragecase, reverse=True) 

def test_BubbleWorst():
    start= time
    assert bubble(worstcase) == bestcase
    print(time()-start)

def test_BubbleBest():
    start= time
    assert bubble(bestcase) == bestcase
    print(time()-start)    
    
def test_BubbleAvg():
    start= time
    assert bubble(avaragecase) == bestcase
    print(time()-start)