import numpy as np

A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

addition_result = A + B

multiplication_result = np.dot(A, B)

transpose_result = multiplication_result.T

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition (A + B):\n", addition_result)
print("Matrix Multiplication (A * B):\n", multiplication_result)
print("Transpose of the Product Matrix:\n", transpose_result)
