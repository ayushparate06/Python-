import numpy as np

# -------------------------------
# a) Generate 4x4 Identity Matrix
# -------------------------------
identity_matrix = np.identity(4)
print("4x4 Identity Matrix:")
print(identity_matrix)

# -----------------------------------------------
# b) Generate Two 3x3 Random Matrices (1 to 9)
#    Perform Addition and Multiplication
# -----------------------------------------------

# Generate random matrices
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)