'''
Suppose we have a polynomial $(x+y)^n$ 
and we want to find the coefficient of $(x^k)(y^n-k)$ such as in a polynomial expansion. Use dynamic programming to solve this problem. Show code in Python. Your solution should involve a matrix. Hint: the first column and first row of the matrix will end up as all 1s. Think Pascal's Triangle

To solve the problem of finding the coefficient of xkyn−kxkyn−k in the expansion of (x+y)n(x+y)n using dynamic programming, we can indeed use a concept similar to Pascal's Triangle. Here's the approach:

    Initialize a Matrix: We'll create a matrix (2D array) where each cell dp[i][j] represents the coefficient of xjyi−jxjyi−j in the expansion of (x+y)i(x+y)i.

    Base Case: The first row and the first column will be initialized to 1s, as in Pascal's Triangle. This represents the fact that the coefficient of yiyi in the expansion of (x+y)i(x+y)i is always 1, and similarly for xixi.

    Fill the Matrix: We fill the rest of the matrix using the relation that each cell is the sum of the cell above and the cell to the left. This is because each term in the expansion of (x+y)n(x+y)n can be formed by either adding an xx or a yy to a term in the expansion of (x+y)n−1(x+y)n−1.

    Retrieve the Desired Coefficient: Finally, we retrieve the value at dp[n][k], which gives the coefficient of xkyn−kxkyn−k in the expansion.
'''

def find_coefficient(n, k):
    # Initialize a 2D matrix with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # The first row and first column will be all 1s
    for i in range(n + 1):
        dp[i][0] = 1
       # dp[0][i] = 1

    # Fill the matrix using the rule from Pascal's Triangle
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j] + dp[i-1][j - 1]

    # The coefficient of x^k * y^(n-k) is now in dp[n][k]
    return dp[n][k]

# Example usage
n = 5
k = 2
print(f"The coefficient of x^{k} y^{n-k} in the expansion of (x+y)^{n} is {find_coefficient(n, k)}")

