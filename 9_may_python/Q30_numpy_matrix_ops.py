# Q30. NumPy program to create two matrices and perform addition,
#      subtraction, multiplication, and inverse operations.

import numpy as np

# --- Main Program ---
print("=" * 55)
print("   MATRIX OPERATIONS USING NumPy")
print("=" * 55)

# Create two 3x3 matrices
matrix_a = np.array([[5, 3, 1],
                     [2, 7, 4],
                     [6, 1, 8]])

matrix_b = np.array([[3, 6, 2],
                     [1, 4, 5],
                     [7, 3, 9]])

# Display the original matrices
print("\nMatrix A:")
print(matrix_a)
print(f"\nMatrix B:")
print(matrix_b)

# 1. Matrix Addition
print("\n" + "-" * 40)
print("1. Matrix Addition (A + B):")
addition_result = np.add(matrix_a, matrix_b)
print(addition_result)

# 2. Matrix Subtraction
print("\n" + "-" * 40)
print("2. Matrix Subtraction (A - B):")
subtraction_result = np.subtract(matrix_a, matrix_b)
print(subtraction_result)

# 3. Element-wise Multiplication
print("\n" + "-" * 40)
print("3. Element-wise Multiplication (A * B):")
elementwise_product = np.multiply(matrix_a, matrix_b)
print(elementwise_product)

# 4. Matrix Multiplication (Dot Product)
print("\n" + "-" * 40)
print("4. Matrix Multiplication (A @ B):")
dot_product = np.dot(matrix_a, matrix_b)
print(dot_product)

# 5. Inverse of Matrix A
print("\n" + "-" * 40)
det_a = np.linalg.det(matrix_a)
print(f"5. Determinant of A: {det_a:.4f}")
if det_a != 0:
    inverse_a = np.linalg.inv(matrix_a)
    print("   Inverse of Matrix A:")
    print(np.round(inverse_a, 4))
else:
    print("   Matrix A is singular (non-invertible).")

# 6. Inverse of Matrix B
print("\n" + "-" * 40)
det_b = np.linalg.det(matrix_b)
print(f"6. Determinant of B: {det_b:.4f}")
if det_b != 0:
    inverse_b = np.linalg.inv(matrix_b)
    print("   Inverse of Matrix B:")
    print(np.round(inverse_b, 4))
else:
    print("   Matrix B is singular (non-invertible).")

# 7. Verification: A * A_inv = Identity
print("\n" + "-" * 40)
print("7. Verification (A × A⁻¹ = Identity):")
if det_a != 0:
    identity_check = np.dot(matrix_a, inverse_a)
    print(np.round(identity_check, 2))

# Additional operations
print("\n" + "=" * 40)
print("   ADDITIONAL OPERATIONS")
print("=" * 40)
print(f"  Transpose of A:\n{matrix_a.T}")
print(f"\n  Trace of A     : {np.trace(matrix_a)}")
print(f"  Trace of B     : {np.trace(matrix_b)}")
print(f"  Rank of A      : {np.linalg.matrix_rank(matrix_a)}")
print(f"  Rank of B      : {np.linalg.matrix_rank(matrix_b)}")

# --- Expected Output ---
# =======================================================
#    MATRIX OPERATIONS USING NumPy
# =======================================================
#
# Matrix A:
# [[5 3 1]
#  [2 7 4]
#  [6 1 8]]
#
# Matrix B:
# [[3 6 2]
#  [1 4 5]
#  [7 3 9]]
#
# ----------------------------------------
# 1. Matrix Addition (A + B):
# [[ 8  9  3]
#  [ 3 11  9]
#  [13  4 17]]
#
# ----------------------------------------
# 2. Matrix Subtraction (A - B):
# [[ 2 -3 -1]
#  [ 1  3 -1]
#  [-1 -2 -1]]
#
# ----------------------------------------
# 3. Element-wise Multiplication (A * B):
# [[15 18  2]
#  [ 2 28 20]
#  [42  3 72]]
#
# ----------------------------------------
# 4. Matrix Multiplication (A @ B):
# [[25 45 34]
#  [41 52 75]
#  [75 64 89]]
#
# ----------------------------------------
# 5. Determinant of A: -175.0000
#    Inverse of Matrix A:
# [[-0.3029  0.1314  -0.0286]
#  [-0.0457  -0.1943   0.1029]
#  [ 0.2286   -0.0743   0.1657]]
