'''
Generated via ChatGPT4 
Example implementatin of Strassen's Algorithm for multiplying Matrices 

'''

import numpy as np

def matrix_multiply(A, B):
    # A is a matrix with dimensions m x n
    # B is a matrix with dimensions n x p
    # The result will be a matrix with dimensions m x p

    m = len(A)
    n = len(B)
    p = len(B[0])

    # Initialize the result matrix with zeros
    result = [[0 for row in range(p)] for col in range(m)]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example usage
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

result = matrix_multiply(A, B)
print("Result:")
for row in result:
    print(row)


def split(matrix):
    """
    Splits a given matrix into quarters.
    Input: nxn matrix
    Output: tuple of 4 matrices corresponding to the quarters of the matrix
    """
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
    """
    Computes matrix product by Strassen's Algorithm.
    Input: nxn matrices x and y
    Output: nxn matrix, product of x and y
    """

    # Base case when size of matrices is 1x1
    if len(x) == 1:
        return x * y

    # Splitting the matrices into quarters
    a, b, c, d = split(x)
    e, f, g, h = split(y)
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)
    print("e = ", e)
    print("f = ", f)
    print("g = ", g)
    print("h = ", h)


    # Computing the 7 products, recursively (p1, p2...p7)
    p1 = strassen(a, f - h)
    p2 = strassen(a + b, h)        
    p3 = strassen(c + d, e)        
    p4 = strassen(d, g - e)        
    p5 = strassen(a + d, e + h)        
    p6 = strassen(b - d, g + h)  
    p7 = strassen(a - c, e + f)

    # Calculating the results from the 7 products
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2 
    c21 = p3 + p4 
    c22 = p1 + p5 - p3 - p7 

    # Combining the 4 quarters into a single matrix by stacking horizontally and vertically
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

    return c

# Example usage
A = np.random.randint(10, size=(4, 4))
B = np.random.randint(10, size=(4, 4))
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Product of A and B by Strassen's Algorithm:\n", strassen(A, B))

print("naive method: ", matrix_multiply(A, B))
