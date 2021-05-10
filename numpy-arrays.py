import numpy as np

# single dimensional
arr1 = np.array([1,2,3])
print (arr1)

# two-dimensional
arr2 = np.array([[23,45],[45,67]])
print (arr2)

# minimum dimension
arr3 = np.array([4,6,3,7], ndmin = 2)
print (arr3)

# dtype
arr4 = np.array([1,2,3], dtype=complex)
print (arr4)

# array with zeroes
arr5 = np.zeros(3)
print (arr5)

# array with ones
arr6 = np.ones(5)
print (arr6)

# empty array
arr7 = np.empty(2)
print (arr7)

# array within a range
arr8 = np.arange(5)
print (arr8)

# array within intervals
arr9 = np.arange(3,12,2)
print (arr9)

# array with linear spacing
arr0 = np.linspace(2,10, num=5)
print (arr0)

# array sort
arr = np.array([2,5,1,7,4,9])

# simple sort
print (np.sort(arr))

# argsort(returns index of elements when sorted)
print (np.argsort(arr))