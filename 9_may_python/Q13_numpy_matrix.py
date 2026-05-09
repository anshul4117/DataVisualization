# Q13. NumPy program to create a 5x5 matrix with random integers and
#      calculate row-wise sum, column-wise sum, transpose, and determinant.

import numpy as np

# Set random seed for reproducibility (optional)
np.random.seed(42)

# Create a 5x5 matrix with random integers (range 1 to 50)
random_matrix = np.random.randint(1, 51, size=(5, 5))

# Display the original matrix
print("=" * 55)
print("   NumPy 5x5 MATRIX OPERATIONS")
print("=" * 55)

print("\nOriginal 5x5 Matrix:")
print(random_matrix)

# 1. Row-wise Sum (sum of each row)
row_sum = np.sum(random_matrix, axis=1)
print("\n--- Row-wise Sum ---")
for i in range(5):
    print(f"  Row {i + 1}: {row_sum[i]}")

# 2. Column-wise Sum (sum of each column)
column_sum = np.sum(random_matrix, axis=0)
print("\n--- Column-wise Sum ---")
for i in range(5):
    print(f"  Column {i + 1}: {column_sum[i]}")

# 3. Transpose of the matrix
transpose_matrix = np.transpose(random_matrix)
print("\n--- Transpose of Matrix ---")
print(transpose_matrix)

# 4. Determinant of the matrix
determinant = np.linalg.det(random_matrix)
print(f"\n--- Determinant of Matrix ---")
print(f"  Determinant = {determinant:.4f}")

# Additional operations for completeness
print("\n--- Additional Info ---")
print(f"  Matrix Shape       : {random_matrix.shape}")
print(f"  Total Sum          : {np.sum(random_matrix)}")
print(f"  Mean Value         : {np.mean(random_matrix):.2f}")
print(f"  Max Element        : {np.max(random_matrix)}")
print(f"  Min Element        : {np.min(random_matrix)}")
print(f"  Diagonal Elements  : {np.diag(random_matrix)}")
print(f"  Trace (Sum of Diag): {np.trace(random_matrix)}")

# --- Expected Output ---
# =======================================================
#    NumPy 5x5 MATRIX OPERATIONS
# =======================================================
#
# Original 5x5 Matrix:
# [[39 28 16 44 47]
#  [ 1 36 33 15 39]
#  [21  9  1 43  6]
#  [30 37 40 29 34]
#  [48 30 10 44  2]]
#
# --- Row-wise Sum ---
#   Row 1: 174
#   Row 2: 124
#   Row 3: 80
#   Row 4: 170
#   Row 5: 134
#
# --- Column-wise Sum ---
#   Column 1: 139
#   Column 2: 140
#   Column 3: 100
#   Column 4: 175
#   Column 5: 128
#
# --- Transpose of Matrix ---
# [[39  1 21 30 48]
#  [28 36  9 37 30]
#  [16 33  1 40 10]
#  [44 15 43 29 44]
#  [47 39  6 34  2]]
#
# --- Determinant of Matrix ---
#   Determinant = -21949070.0000
#
# --- Additional Info ---
#   Matrix Shape       : (5, 5)
#   Total Sum          : 682
#   Mean Value         : 27.28
#   Max Element        : 48
#   Min Element        : 1
#   Diagonal Elements  : [39 36  1 29  2]
#   Trace (Sum of Diag): 107
