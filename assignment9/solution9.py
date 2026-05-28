import numpy as np

# Q1: Replace NaN with 0 and interchange 3 rows and 3 columns
arr = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
print("Original array:\n", arr)

arr[np.isnan(arr)] = 0
print("After replacing NaN with 0:\n", arr)

rows = arr[[0, 1, 0], :]
print("3 rows interchanged:\n", rows)

cols = arr[:, [0, 1, 2]]
print("3 columns selected:\n", cols)


# Q2: Move axes of a 3D array to new positions
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Original shape:", arr3d.shape)
print("Original array:\n", arr3d)

moved = np.moveaxis(arr3d, 0, 2)
print("After moveaxis (0 -> 2), shape:", moved.shape)
print(moved)


# Q3: Replace NaN values with average of columns
arr2 = np.array([[1, np.nan, 3],
                 [4, 5, np.nan],
                 [7, 8, 9]], dtype=float)
print("Original array:\n", arr2)

col_mean = np.nanmean(arr2, axis=0)
print("Column averages:", col_mean)

for j in range(arr2.shape[1]):
    for i in range(arr2.shape[0]):
        if np.isnan(arr2[i, j]):
            arr2[i, j] = col_mean[j]

print("After replacing NaN with column mean:\n", arr2)


# Q4: Replace negative values with zero
arr4 = np.array([3, -1, -7, 5, -2, 8])
print("Original array:", arr4)

arr4[arr4 < 0] = 0
print("After replacing negatives with 0:", arr4)
