import unittest
def knapsack(W, weights, values, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][W]

class TestKnapsack(unittest.TestCase):
    
    def test_knapsack(self):
        W = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(weights)

if __name__ == '__main__':
    unittest.main()
