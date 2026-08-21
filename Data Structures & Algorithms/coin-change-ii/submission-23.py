class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            coin = coins[i-1]
            for x in range(amount+1):
                dp[i][x] = dp[i-1][x]
                if coin <= x:
                    dp[i][x] += dp[i][x - coin]
        return dp[n][amount]