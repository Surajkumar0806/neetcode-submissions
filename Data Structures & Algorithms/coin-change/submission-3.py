class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            coin = coins[i-1]
            for x in range(1, amount + 1):
                skip = dp[i-1][x]
                if coin <= x:
                    take = 1 + dp[i][x - coin]
                    dp[i][x] = min(skip, take)
                else:
                    dp[i][x] = skip
        return dp[n][amount] if dp[n][amount] != float('inf') else -1