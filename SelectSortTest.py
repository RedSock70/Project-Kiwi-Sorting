# from random import randint, random
# from select import select
# from SelectSortKiwi import bubble
# from time import time

# avaragecase= [randint(1,10000) for _ in range(1000)]
# bestcase= sorted(avaragecase)
# worstcase= sorted(avaragecase, reverse=True) 

# def test_SelectWorst():
#     start= time
#     assert select(worstcase) == bestcase
#     print(time()-start)

# def test_SelectBest():
#     start= time
#     assert select(bestcase) == bestcase
#     print(time()-start)    
    
# def test_SelectAvg():
#     start= time
#     assert select(avaragecase) == bestcase
#     print(time()-start)

from ctypes import sizeof
from random import randint, random
import numpy as np
from SelectSortKiwi import selectionSort, data
from time import time

# avaragecase= [randint(1,10000) for _ in range(1000)]
# bestcase= sorted(avaragecase)
# worstcase= sorted(avaragecase, reverse=True) 
cum = data
avaragecase = cum
bestcase = np.sort(avaragecase)
worstcase = bestcase[::-1]
def test_SelectWorst():
    start= time()
    assert np.array_equal( selectionSort(np.copy(worstcase), len(worstcase)) , bestcase)
    print(str(time()-start))

def test_SelectBest():
    start= time()
    assert np.array_equal( selectionSort(np.copy(bestcase), len(bestcase)) , bestcase)
    print(str(time()-start))
    
def test_SelectAvg():
    start= time()
    assert np.array_equal( selectionSort(np.copy(avaragecase), len(avaragecase)) , bestcase)
    print(str(time()-start))