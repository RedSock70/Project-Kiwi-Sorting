# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [2.049,2.398,2.009,1.809,2.894,2.054,2.927,2.848,2.246,1.971,2.432,2.739,2.256,3.167,2.289,2.462,2.044,1.951,2.455,3.719,2.586,1.644,2.994,2.5,2.331,2.21,3.101,2.204,2.289,2.633,2.675,2.47,2.253,1.67,3.142,2.799,2.686,2.159,3.101,2.457,2.542,2.758,2.933,2.299,2.563,3.017,2.908,3.116,2.505,2.125,2.33,2.141,3.138,2.297,2.713,2.662,3.668,3.453,2.48,2.612,3.445,2.302,2.461,2.168,3.397,2.371,2.835,1.824,2.691,2.506,2.853,2.794,2.572,3.471,2.026,2.896,3.222,2.454,1.905,2.322,2.411,1.679,2.817,2.549,2.206,2.418,2.914,3.822,3.27,2.258,3.294,2.745,2.643,3.313,2.057,2.393,2.389,2.377,2.102,3.26,2.135,2.929,2.387,2.787,2.367,1.959,2.414,3.436,2.172,3.033,2.085,2.213,2.834,1.61,2.89,2.612,2.7]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)


print('Sorted Array in Ascending Order:')
print(data)