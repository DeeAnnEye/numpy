import numpy as np

# single dimensional
arr1 = np.array([1, 2, 3])
print(arr1)

# two-dimensional
arr2 = np.array([[23, 45], [45, 67]])
print(arr2)

# minimum dimension
arr3 = np.array([4, 6, 3, 7], ndmin=2)
print(arr3)

# dtype
arr4 = np.array([1, 2, 3], dtype=complex)
print(arr4)

# array with zeroes
arr5 = np.zeros(3)
print(arr5)

# array with ones
arr6 = np.ones(5)
print(arr6)

# empty array
arr7 = np.empty(2)
print(arr7)

# array within a range
arr8 = np.arange(5)
print(arr8)

# array within intervals
arr9 = np.arange(3, 12, 2)
print(arr9)

# array with linear spacing
arr0 = np.linspace(2, 10, num=5)
print(arr0)

# array sort
arr = np.array([2, 5, 1, 7, 4, 9])

# simple sort
print(np.sort(arr))

# argsort(returns index of elements when sorted)
print(np.argsort(arr))

# two dimensional array argsort
x = np.array([[0, 3], [2, 2]])

# gets index
x_sort = np.argsort(x, axis=0)

# gets actual array
print(np.take_along_axis(x, x_sort, axis=0))

ind = np.unravel_index(np.argsort(x, axis=None), x.shape)
print(x[ind])

# sort on Axes
y = np.array([(1, 0), (0, 1)], dtype=[('x', '<i4'), ('y', '<i4')])
print(np.argsort(y, order=('y', 'x')))

# array dtype
dt = np.dtype([('count', np.int8)])
p = np.array([10, 20, 40], dt)
print(p['count'])

stDt = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
student = np.array([('Mark', 36, 54.2), ('James', 23, 76.8)], dtype=stDt)
print(student)

# array indexing (single dimension)
s = np.array([1, 2, 3, 4, 5])
print(s[4])

# array indexing (multi-dimension)
r = np.array([[1, 2], [3, 4]])
print(r[1, 1])

# reshape
t = np.array([1, 2, 3, 4, 5, 6])
st = t.reshape(2, 3)
print(st)

# iteration (1d)
f = np.array([1, 2, 3, 4, 5])
for x in f:
    print(x)

# iteration (2d)
l = np.array([[1, 2, 3], [4, 5, 6]])
for x in l:
    print(x)

# nditer (iterate on scalar element)
nd = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [4, 5, 7]]])
for x in np.nditer(nd):
    print(x)

# change datatype on iteration
adt = np.array([1, 2, 3, 4, 5])
for x in np.nditer(adt, flags=['buffered'], op_dtypes='S'):
    print(x)

# iterate with step-size
step_arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(step_arr[:, ::2]):
    print(x)

# ndenumerate
q = np.array([1, 2, 3, 4, 5])
for idx, x in np.ndenumerate(q):
    print(idx, x)

# shape
t = np.array([[2, 3, 4], [5, 6, 7]])
print(t.shape)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b.shape = (4, 2)
print(b)

# list to array
h = [1, 5, 6]
a = np.asarray(h, dtype=float)
print(a)

# frombuffer
e = b'Hello world'
j = np.frombuffer(e, dtype='S1') 
print(j)

# fromiter
u = range(5)
i = iter(u)

xp = np.fromiter(i, dtype=float)
print(xp)