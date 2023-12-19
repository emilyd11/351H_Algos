''' Generated via ChatGPT ''' 

def knapsack_0_1(values, weights, capacity):
    """
    Solve the 0-1 Knapsack problem using dynamic programming.

    :param values: List of values of the items.
    :param weights: List of weights of the items.
    :param capacity: Maximum weight capacity of the knapsack.
    :return: Maximum value that can be put in a knapsack of given capacity.
    """
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            '''else:
                dp[i][w] = dp[i - 1][w] '''

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]   # Weights of the items
capacity = 50            # Capacity of the knapsack

max_value = knapsack_0_1(values, weights, capacity)
print("Maximum value in knapsack =", max_value)
