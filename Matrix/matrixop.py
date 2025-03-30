import numpy as np

A = np.random.randint(0, 21, (3, 3))
B = np.random.randint(0, 21, (3, 3))

addition_result = A + B

multiplication_result = np.dot(A, B)   #use of the numpy library

transpose_result = multiplication_result.T

print("Matrix A:\n", A) #matrix A
print("Matrix B:\n", B) #matrix B
print("Matrix Addition (A + B):\n", addition_result)  #gives the sum of matrixes
print("Matrix Multiplication (A * B):\n", multiplication_result) #provides the result of multiplaication of the matrixes
print("Transpose of the Product Matrix:\n", transpose_result) #gives the transpose of the matrix
