from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize memoization table
        memo = [-1] * (amount + 1)
        memo[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # Call the helper function to calculate the minimum coins
        return self.coinChangeHelper(coins, amount, memo)

    def coinChangeHelper(self, coins: List[int], amount: int, memo: List[int]) -> int:
        # If the amount is negative, return -1 (invalid case)
        if amount < 0:
            return -1
        
        # If the result is already computed, return it
        if memo[amount] != -1:
            return memo[amount]

        # Initialize the minimum number of coins as infinity
        minCoins = float("inf")
        
        # Try using each coin
        for coin in coins:
            res = self.coinChangeHelper(coins, amount - coin, memo)
            if res >= 0:  # Valid result
                minCoins = min(minCoins, res + 1)
        
        # If no valid coin combinations, memoize as -1 (not possible)
        memo[amount] = -1 if minCoins == float("inf") else minCoins
        return memo[amount]
