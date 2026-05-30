import numpy as np
from scipy import stats

# 3D array
arr = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])
print(arr)
print(arr.shape)
print(arr[0, 1, 2])

# zeros 3D
x = np.zeros((2, 3, 4))
print(x)

# array() function
a = np.array([1, 2, 3, 4], dtype=float)
print(a)

b = np.array([[1, 2], [3, 4]], ndmin=3)
print(b)
print(b.shape)

# copy vs view
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

# shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

# ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.shape)

# reshape 1D to 2D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.reshape(4, 3))

# reshape 1D to 3D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.reshape(2, 3, 2))

# flatten
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(-1))

# iterate 1D
arr = np.array([1, 2, 3, 4, 5])
for element in arr:
    print(element)

# iterate 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for row in arr_2d:
    print(row)

# nditer
arr = np.array([[1, 2], [3, 4]])
for x in np.nditer(arr):
    print(x)

# array operations
a = np.array([[12, 53, 25, 75], [4, 6, 8, 10], [9, 7, 5, 3], [47, 92, 13, 71]], dtype=int)
print(a)
print(a.reshape(8, 2))

a2 = np.array([[1, 2, 3], [4, 5, 6]])
print(np.reshape(a2, (3, 2), order='F'))

print(a.ravel())
print(np.unique(a))
print(a.min(), a.max())
print(a.sum())
print(a.sum(axis=1))
print(np.std(a))
print(np.sqrt(a))

# two array operations
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10, 11, 1], [13, 14, 1]])
print(a + b)
print(a * b)
print(a / b)
print(a - b)

b = np.array([[10, 11], [13, 14], [1, 2]])
print(a.dot(b))

a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(a.dot(b))

# pad
array = np.array([1, 2, 3])
print(np.pad(array, pad_width=2, mode='constant'))

# transpose
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.transpose(array_2d))

# concatenate
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(np.concatenate((array1, array2)))

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((array1, array2), axis=0))
print(np.concatenate((array1, array2), axis=1))

# split
arr = np.arange(9)
print(arr)
result = np.split(arr, 3)
for i, sub_array in enumerate(result):
    print(f"Sub-array {i+1}:", sub_array)

# resize
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
b = np.resize(a, (3, 2))
print(b)
print(b.shape)
b = np.resize(a, (3, 3))
print(b)

# append
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.append(a, [7, 8, 9]))
print(np.append(a, [[7, 8, 9]], axis=0))
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))

# insert
a = np.array([[1, 2], [3, 4], [5, 6]])
print(np.insert(a, 3, [11, 12]))

# delete
a = np.arange(12).reshape(3, 4)
print(np.delete(a, 5))

# flip
my_array = np.array([10, 20, 30, 40, 50])
print(np.flip(my_array))

# sort
a = np.array([25, 5, 15, 10])
b = np.sort(a)
print(b)

# argmax argmin
array = np.array([10, 20, 5, 30, 15])
print(np.argmax(array))
print(np.argmin(array))

# indexing
a = np.arange(10)
print(a[6])

arr = np.arange(6)
print(arr[-2:])

arr = np.arange(12)
print(arr[::2])

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(arr[:, 1])

# average mean median mode
arr1 = np.array([[3, 4], [2, 8]])
arr2 = np.array([[1, 0], [4, 3]])
avg = (arr1 + arr2) / 2
print(avg)
print(np.mean(arr1))
print(np.mean(arr2))
print(np.median(arr1))
print(np.median(arr2))
print(stats.mode(arr1.flatten()).mode)
print(stats.mode(arr2.flatten()).mode)
