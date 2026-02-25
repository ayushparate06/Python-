import numpy as np

# -----------------------------
# Input for 5x3 Matrix
# -----------------------------
print("Enter elements for 5x3 matrix:")

matrix1 = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1} separated by space: ").split()))
    matrix1.append(row)

matrix1 = np.array(matrix1)

# -----------------------------
# Input for 3x2 Matrix
# -----------------------------
print("\nEnter elements for 3x2 matrix:")

matrix2 = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1} separated by space: ").split()))
    matrix2.append(row)

matrix2 = np.array(matrix2)

# -----------------------------
# Matrix Multiplication
# -----------------------------
product = np.dot(matrix1, matrix2)

# -----------------------------
# Display Result
# -----------------------------
print("\n5x3 Matrix:")
print(matrix1)

print("\n3x2 Matrix:")
print(matrix2)

print("\nProduct Matrix (5x2):")
print(product)