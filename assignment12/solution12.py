import numpy as np

# 1. Convert 1D array to 2D & Print Array Attributes
print("--- 1. Array Conversion and Attributes ---")
arr_1d = np.array([1, 2, 3, 4, 5, 6])

arr_2d = arr_1d.reshape(2, 3)
print("2D Array:\n", arr_2d)

print("Shape:", arr_2d.shape)          
print("Dimensions:", arr_2d.ndim)     
print("Data Type:", arr_2d.dtype)       
print("Item Size (bytes):", arr_2d.itemsize) 

# 2. Create a 3×3 NumPy array of all 9
print("\n--- 2. 3x3 Array of All 9s ---")
arr_nines = np.full((3, 3), 9)
print(arr_nines)

# 3. Create a 1D array of 10 evenly spaced values between 25 and 125
print("\n--- 3. Evenly Spaced Values ---")
arr_spaced = np.linspace(25, 125, 10)
print(arr_spaced)

# 4. Convert a Python list into a NumPy array
print("\n--- 4. Python List to NumPy Array ---")
py_list = [10, 20, 30, 40, 50]
arr_from_list = np.array(py_list)
print("NumPy Array:", arr_from_list)

# 5. Reverse a 1D NumPy array
print("\n--- 5. Reverse 1D Array ---")
orig_arr = np.array([1, 2, 3, 4, 5])
reversed_arr = orig_arr[::-1]
print("Original:", orig_arr)
print("Reversed:", reversed_arr)

# 6. Create a 4×4×3 array and extract value at second set, first row, last column
print("\n--- 6. 4x4x3 Indexing ---")
arr_3d = np.arange(1, 49).reshape(4, 4, 3)

extracted_val = arr_3d[1, 0, -1]
print("Extracted Value:", extracted_val)

# 7. Create a 4×4 and Extract Odd Rows and Even Columns
print("\n--- 7. 4x4 Slicing (Odd Rows, Even Columns) ---")
matrix_4x4 = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 Matrix:\n", matrix_4x4)

extracted_subgrid = matrix_4x4[1::2, 0::2]
print("Extracted Subgrid:\n", extracted_subgrid)

# 8. Slice first two rows and first two columns of second set from a 4×4×3 array
print("\n--- 8. 4x4x3 Sub-slicing ---")
sub_slice = arr_3d[1, 0:2, 0:2]
print("Sliced 2x2 Region from Second Set:\n", sub_slice)

# 9. Replace all odd numbers with -1 using a for loop
print("\n--- 9. Replace Odd Numbers via Iteration ---")
arr_to_modify = np.array([[23, 56, 78, 93], [71, 82, 13, 24]])
print("Before modification:\n", arr_to_modify)

for i in range(arr_to_modify.shape[0]):
    for j in range(arr_to_modify.shape[1]):
        if arr_to_modify[i, j] % 2 != 0:
            arr_to_modify[i, j] = -1

print("After replacing odds with -1:\n", arr_to_modify)

# 10. Get the indices of non-zero elements
print("\n--- 10. Non-zero Element Indices ---")
nonzero_arr = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(nonzero_arr)
print("Indices of non-zero elements:", indices[0])

# 11. Perform arithmetic operations on two NumPy arrays element-wise
print("\n--- 11. Element-wise Arithmetic ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

add_result = np.add(a, b)        
mul_result = np.multiply(a, b)   

print("Array A:", a)
print("Array B:", b)
print("Element-wise Addition (np.add):", add_result)
print("Element-wise Multiplication (np.multiply):", mul_result)

# 12. Compute the dot product of two NumPy arrays
print("\n--- 12. Dot Product ---")
arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])

dot_product = np.dot(arr1, arr2)
print("Arr1:", arr1)
print("Arr2:", arr2)
print("Dot Product:", dot_product)
