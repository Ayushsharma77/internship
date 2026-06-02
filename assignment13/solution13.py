import numpy as np
import matplotlib.pyplot as plt

print("--- Problem 1 ---")
arr1 = np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
arr1 = np.nan_to_num(arr1, nan=0)
arr1[[0, 1], :] = arr1[[1, 0], :]
arr1[:, [0, 1, 2]] = arr1[:, [1, 2, 0]]
print("Manipulated Array:\n", arr1, "\n")

print("--- Problem 2 ---")
arr_3d = np.arange(24).reshape(2, 3, 4)
moved_arr = np.moveaxis(arr_3d, source=0, destination=2)
print("New array shape after moving axis:", moved_arr.shape, "\n")

print("--- Problem 3 ---")
arr_nan = np.array([[1.0, 2.0, np.nan], [4.0, np.nan, 6.0], [7.0, 8.0, 9.0]])
col_means = np.nanmean(arr_nan, axis=0)
inds = np.where(np.isnan(arr_nan))
arr_nan[inds] = np.take(col_means, inds)
print("Array after column mean replacement:\n", arr_nan, "\n")

print("--- Problem 4 ---")
arr_neg = np.array([12, -5, 33, -1, 0])
arr_neg[arr_neg < 0] = 0
print("Array after replacing negatives:", arr_neg, "\n")

print("--- Problem 5 ---")
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])
combined = np.array([a1, a2])
mean_val = np.mean(combined)
median_val = np.median(combined)
vals, counts = np.unique(combined, return_counts=True)
mode_val = vals[np.argmax(counts)]
print(f"Combined Mean: {mean_val}")
print(f"Combined Median: {median_val}")
print(f"Combined Mode (Pure NumPy): {mode_val}\n")

print("--- Problem 6 ---")
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
b = np.array([9, -6, 17])
A_inv = np.linalg.inv(A)
solution = np.dot(A_inv, b)
print("Solutions [x, y, z]:", solution, "\n")

print("--- Problem 7 ---")
semesters = np.array(['Semester 1', 'Semester 2'])
gpa = np.array([8.2, 8.9])
plt.figure(figsize=(6, 4))
plt.plot(semesters, gpa, label='GPA Trend', color='red', linewidth=2, marker='o')
plt.title('Semester Academic Results Comparison')
plt.xlabel('Semesters')
plt.ylabel('GPA / Marks')
plt.ylim(0, 10)
plt.legend()
plt.grid(True, linestyle='--', color='gray', alpha=0.6)
print("Plot configurations defined. Call plt.show() to view.")
# plt.show()
